# Pi-Led-Web-App
This project drives a LED via a simple web application.

### Motivation
I come from the embedded background. I wanted to move up to the application level.

### Installation
I use virtualenv, a tool to create isolated Python environments.
http://flask.pocoo.org/docs/0.11/installation/
 
 To quickly install the required packages :
```sh
$ pip install -r ./Pi-LED-Web-App/requirements.txt
```

### Start instructions

To start the server :
```sh
$ python webapp.py
```

To drive the LED:
http://MyPiHostName.local:8000/
MyPiHostName is the host name of your own Raspberry.
