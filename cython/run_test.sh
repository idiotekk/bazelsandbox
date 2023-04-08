test_name=test_copy_dir
workspace_root=$(bazel info workspace)
bazel test $test_name --test_output=all