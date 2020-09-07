# README


## Installation 

USE `Python 3.6.5`

### Script:

```bash
source setup.sh
```

### Manual: 

setup virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

install requirements

```bash
pip3 install -r requirements.txt
```

## Run

### development

```bash
    python3 manage.py runserver
```

### production

1. Open deploy.sh and enter your domain in the variable `DOMAIN`

2. Run deploy.sh
```bash
    source deploy.sh
```


