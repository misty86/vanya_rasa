# Installation
1. Install [python3.10](https://www.python.org/downloads/release/python-31011/)
2. Install [poetry](https://python-poetry.org/docs/#installation)
3. Install [ngrok](https://ngrok.com/download) for tg example
# Create env
1. run ```cd rasa_vanya```
2. run ```poetry env use python3.10```
3. run ```pip3 install rasa```
# Train
1. ```rasa train```
# Run
1. run action server ```rasa run actions```
2. run rasa ```rasa run --enable-api```
# Post request example
```curl --location --request POST 'http://0.0.0.0:5005/model/parse' --header 'Content-Type: application/json' --data-raw '{"text": "тест"}'```