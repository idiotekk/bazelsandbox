import os
import sys
from pathlib import Path
import json
try:
    from unknownlib import *
except ModuleNotFoundError as e:
    print(json.dumps({"sys.path": sys.path}, indent=4))
    raise e


if __name__ == "__main__":

    print_tree(Path(__file__).parents[2])
    print_tree(os.getenv("TEST_SRCDIR"))
    print_tree(os.getenv("TEST_TMPDIR"))
    input_dir = Path(__file__).parent / "tmp"
    output_dir = Path(__file__).parent / "output"
    copy_dir(input_dir, output_dir)
    assert directories_identical(input_dir, output_dir)