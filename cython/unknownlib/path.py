import os
import shutil
import fnmatch
import logging
import filecmp
from typing import Union, List
from pathlib import Path
from glob import glob

logging.basicConfig(level=logging.INFO, format="%(funcName)s: %(message)s")


def copy_dir(src_dir: Union[str, Path],
             dst_dir: Union[str, Path],
             patterns: List[Union[str, Path]]=["**"]):
    """ Copy a directory recursively.
    Filter for `patterns`.
    """
    assert os.path.isdir(str(src_dir)), f"{src_dir} is not a directory"
    files = glob(f"{src_dir}/**/*", recursive=True)
    files = [_ for _ in files if any(fnmatch.fnmatch(_, p) for p in patterns) and os.path.isfile(_)]
    logging.info(f"number of files: {len(files)}")
    for src_file in files:
        dst_file = Path(dst_dir) / Path(src_file).relative_to(Path(src_dir))
        dst_file.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"copying {src_file} to {dst_file}")
        shutil.copy(src_file, dst_file)
    logging.info("done.")
        
        
def print_tree(dir_):
    assert os.path.isdir(str(dir_)), f"{dir_} is not a directory"
    s = os.popen(f"cd {dir_}; tree").read()
    logging.info(f"""{dir_}\n{s}""")


def directories_identical(dir1, dir2):
    cmp_result = filecmp.dircmp(dir1, dir2)
    if len(cmp_result.left_only) > 0 or len(cmp_result.right_only) > 0:
        logging.info(cmp_result)
        return False
    for common_dir in cmp_result.common_dirs:
        if not directories_identical(f"{dir1}/{common_dir}", f"{dir2}/{common_dir}"):
            return False
    for common_file in cmp_result.common_files:
        if not filecmp.cmp(f"{dir1}/{common_file}", f"{dir2}/{common_file}"):
            return False
    return True