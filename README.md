# Proyecto del curso de PIP y entornos virtuales

## Como Correr el juego:
``` bash
cd game
python3 main.py
```

## Como correr el servidor de uvicorn
``` bash
git clone
cd web-server
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
uvicorn main:app --reload
```