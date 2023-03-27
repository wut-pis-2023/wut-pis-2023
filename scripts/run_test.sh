#!/bin/bash

venv_name="venv"

if [ ! -d "$venv_name" ]
then
    echo "Wirtualne środowisko nie istnieje. Tworzenie..."
    ./skrypt1.sh
fi

source $venv_name/bin/activate

pytest --cov=app tests/

deactivate
