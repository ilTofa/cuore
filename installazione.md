### Prerequisiti

**Python**: Installare python 3, lo scaricate dal [sito](https://www.python.org/downloads/). Provate prima a vedere se è già installato (potrebbe) eseguendo `python3` dalla command line)

**pip**: installatelo da [qui](https://pip.pypa.io/en/stable/installing/), anche in questop caso solo se necessario (provate `pip` dalla command line per vedere se c'è già, dovrebbe)

**git**: se non è compresa nel vostro sistema installatela (per [Windows](https://git-scm.com/download/win))

### Installazione

Aprite un prompt dei comandi ed andate in una cartella conosciuta. Se siete su Mac `cd ~/Desktop/` vi porta sulla scrivania (che rende più semplice aprire i file successivamente).

Create un virtual environment ed attivatelo: 

`python3 -m venv cuore`

`cd cuore`

`source bin/activate`

Scaricate il sorgente da github:

`git clone https://github.com/ilTofa/cuore.git`

Installate i requirements:

`cd cuore`

`pip install -r requirements.txt`

Far partire l'applicazione

`export FLASK_APP=cuore.py`

`export FLASK_DEBUG=1`

`flask run`

A questo punto potete provare l'applicazione, aprire il vostro browser preferito e scrivete nella barra degli indirizzi: `http://127.0.0.1:5000/`
