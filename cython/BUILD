load("@rules_python//python:defs.bzl", "py_library", "py_test")

py_library(
    name = "unknownlib",
    srcs = glob(["unknownlib/**"]),
    deps = [],
    visibility = ["//visibility:public"],
    imports = ["."],
)

py_test(
    name = "test_copy_dir",
    srcs = ["test/test_copy_dir.py"],
    data = ["test/gold", "test/tmp"],
    deps = [":unknownlib"]
)