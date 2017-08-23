# FBmessenger_AI
A demo Python code for FB messenger chatBot\
Author: Min Zhang
# Requirements
* Python 3.X
* pywit
* flask
# pywit
**pywit** is the Python SDK for Wit.ai.
## install
**using pip** :
pip install wit
## Usage for Wit
**wit( access_token )** : Wit constructor 
> * __access_token__ - the access token of your Wit instance

**.message()** : The Wit message API.

> Returns the extracted meaning from a sentence, based on the app data.\
Takes the following parameters:
* __msg__ - the text you want Wit.ai to extract the information from
* __verbose__ - (optional) if set, calls the API with verbose=true

# heroku setup
(https://blog.hartleybrody.com/fb-messenger-bot/)
## login heroku
heroku login
## active virtual env
source env/bin/activate
## chose repository
heroku git:remote -a salty-cliffs-24902
## Deploy your changes
git add .\
git commit -am "make it better"\
git push heroku master
