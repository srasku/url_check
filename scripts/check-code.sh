#!/bin/sh

PY_FILES="url_check/*.py tests/*.py"
pycodestyle $PY_FILES
