$venv_name = "venv"

if (!(Test-Path $venv_name)) {
    Write-Host "Wirtualne środowisko nie istnieje. Tworzenie..."
    & ./install_venv.ps1
}

& $venv_name/Scripts/Activate.ps1

pytest --cov=app tests/

deactivate
