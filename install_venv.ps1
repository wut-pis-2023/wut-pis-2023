$venv_name = "venv"

if (!(Test-Path $venv_name)) {
    & python -m venv $venv_name
}

$activate_script = Join-Path $venv_name "Scripts\Activate.ps1"
& $activate_script

$requirements_file = "requirements.txt"
if (Test-Path $requirements_file) {
    & pip install -r $requirements_file
}

deactivate
