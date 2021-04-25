#!/bin/sh

set -xe
PY_FILES="url_check/*.py tests/*.py"
pycodestyle $PY_FILES
pylint $PY_FILES
