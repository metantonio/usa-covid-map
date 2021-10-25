echo Carpeta de Instalacion de dependencias

cd /d %~dp0
@echo off
cd %

@echo on
pip3 install pandas
echo en caso de repetir instalacion pip3 uninstall matplotlib
python3 -m pip install --upgrade pip
pip3 install matplotlib
pip3 install plotly_express==0.4.0
pip install -U kaleido

python -m pip install --upgrade pip
echo para la instalación correcta
python3 -m pip install matplotlib --user
python3 -m pip install plotly_express==0.4.0
python3 -m pip install kaleido --user

echo END
PAUSE