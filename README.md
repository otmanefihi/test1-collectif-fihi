## Lancement

python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
python app.py

## Verification

python -m unittest discover -v
curl -i http://127.0.0.1:5000/