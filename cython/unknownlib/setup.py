from setuptools import setup
from Cython.Build import cythonize

if __name__ == "__main__":

    setup(
        name="unknownlib",
        packages=["unknownlib"],
        ext_modules=cythonize(
            "unknownlib/**/*.py",
            compiler_directives={'language_level': "3"}
        ),
    )