rm -rf unknownlib
rm -rf build
cp -r ../unknownlib ./
#cythonize -a compiled/unknownlib/**
mkdir -p ../compiled
python ../unknownlib/setup.py build_ext --build-lib ../compiled
rm -rf unknownlib
rm -rf build