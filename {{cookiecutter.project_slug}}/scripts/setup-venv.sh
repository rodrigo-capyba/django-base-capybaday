#!/usr/bin/env bash

if [ ! -d venv ]; then
    if command -v python > /dev/null; then
        mkdir venv && python -m venv venv
    elif command -v python3 > /dev/null; then
        mkdir venv && python3 -m venv venv
    fi
fi

source venv/bin/activate && pip install --upgrade pip && pip install -r requirements/local.txt
