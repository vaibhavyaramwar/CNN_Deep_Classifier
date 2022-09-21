echo [$(date)]: "START"
echo [$(date)]: "Creating env with python 3.8 version"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "Activating the environment"
source activate ./venv
echo [$(date)]: "Installing Dev Requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"