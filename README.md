# python-test

## dev
```
cd dev
```

start
```
pipenv shell
export FLASK_APP="../app/app"
```

run
```
flask run --debug -p 5001
```

out requirements
```
pipenv requirements > ../app/requirements.txt
```

## docker
```
cd docker
```
run
```
cd docker
docker-compose up -d
```
