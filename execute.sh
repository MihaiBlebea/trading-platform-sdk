#!/bin/bash

export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH="${PYTHONPATH}:${PWD}"
eval "./env/bin/python3 -u ./trading_platform/${1}.py ${@:2}"