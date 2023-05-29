#!/bin/bash

venv_name="venv"

if [ ! -d "$venv_name" ]
then
    python -m venv $venv_name
fi

source $venv_name/bin/activate

requirements_file="requirements.txt"
if [ -f "$requirements_file" ]
then
    pip install -r $requirements_file
fi

deactivate
