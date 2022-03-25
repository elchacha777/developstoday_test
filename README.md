# developstoday_test


Test task

### Run project without Docker

Create virtual environment

```bash
python3 -m venv venv
```

Activate virtual enviroment

```bash
. venv/bin/activate
```

Install requirements

```bash
pip3 install -r requirements.txt
```

Create .env, .database.env 
[Example](.example)


```bash
python3 manage.py migrate
```

Run
```bash
python3 manage.py runserver
```

env file
[Example](.example)


### Docker

```bash
docker-compose build
docker-compose up
```


## Deploy
GCP deploy 

http://146.148.99.78/api/v1/register/

## Documentation


* Postman docs [docs](https://documenter.postman.com/preview/15005036-94262c53-60fa-4968-8d48-0e69d77c210e?environment=&versionTag=latest&apiName=CURRENT&version=latest&documentationLayout=classic-double-column&right-sidebar=303030&top-bar=FFFFFF&highlight=EF5B25)


Format and Typing

Pyright
```bash
pyright .
```

Flake8
```bash
flake8 --ignore E501 .
```

Black
```bash
black .
```



