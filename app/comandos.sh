# Cria ambiente virtual
python3 -m venv .venv

# Ativa ambiente virtual
source .venv/bin/activate

# Baixar os requirements
pip install -r requirements.txt

# Rodar aplicação
python3 app.py