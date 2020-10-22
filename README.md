# Floyd-api
api to provide financial data to Floyd


### For DB Migrations:
##### From ./floyd-api:
Update `model.py` with the changes to the model, then run:
```
$ python models/model.py db migrate
```
After you have checked that the SQLAlchemy migrate script is correct, run:
```
$ python models/model.py db upgrade
```