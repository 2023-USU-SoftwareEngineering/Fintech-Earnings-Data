# Fintech Earnings Data
This repository contains a django web server that pulls information from financial APIs and uses trend prediction and NLP to predict the future prices of stocks for tech companies, such as Apple and Google.

# Getting Started
After cloning this repo, ensure you have the packages `django` and `django-cors-headers` installed (run `pip install django` to install django). Navigate to the [fintech_django](fintech_django) directory, and run the command `py manage.py runserver` to start the server at the address `http://localhost:8000`. See the folder's README for more information on using the server.

# Folder Summaries
## fintech_django
This folder contains the django server. The folder's [readme](fintech_django/README.md) contains information on how to run the server.

## fintechrouted
This folder contains code that was used to assemble the vue webapp, which was later ported into django. It currently is not part of the end-product.

## PredictionModels
This folder contains our prediction models, stored in [FintechPredictionModels.ipynb](PredictionModels/FintechPredictionModels.ipynb).

## sqlite
This folder contains the database(s) used for storing stock price history and predictions, as well as scripts that allow us to interact with the database from our web server or our machine learning notebooks.
