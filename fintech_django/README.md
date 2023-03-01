# Django
The server can be started by navigating to this directory and running the command:
```
python manage.py runserver
```
The web application will then be visible from `http://localhost:8000`.

### Specifying a URL

Optionally, you can include a url as an argument, followed by `:8000` to specify the url and port that the server 
should be accessible from. If running from the mater server, the command full command should be:
```
python manage.py runserver mater.cs.usu.edu:8000
```

The web application will then be visible at the address `http://mater.cs.usu.edu:8000`. Stop the server by pressing `CTRL+c` in the console.

### Admin panel

The admin panel is accessible at `http://mater.cs.usu.edu:8000/admin`. 

Login username: `admin`

Login password: `fintech`

Eventually this will be changed, we'll likely create admin accounts for everyone that needs one.

Here, all automation scripts will be visible as hyperlinks in the top-right.

# How to use APIs

### Get companies
URL:
```
http://<insert url here>:8000/companies/list
```
This will return a JSON object of all companies present in the database.

### History
URL:
```
http://<insert url here>:8000/history/pull?OPTIONS
```
Where `OPTIONS` includes the following:
* company = Google | Apple | Amazon, etc.
* from = yyyy.mm.dd
* to = yyyy.mm.dd

For instance, to get Google's history from 2020/01/01 to 2021/01/01:
````
http://<insert url here>:8000/history/pull?company=Google&from=2020.01.01&to=from=2021.01.01
````
This will return a JSON object inluding the history.

### Prediction
URL:
```
http://<insert url here>:8000/prediction/pull?COMPANY
```
Where `COMPANY` is replaced by the following:
* company = Google | Apple | Amazon, etc.

For instance, to get the prediction engine's prediction on Apple:
```
http://<insert url here>:8000/prediction/pull?company=Apple
```
This will return a JSON object of the company's prediction.