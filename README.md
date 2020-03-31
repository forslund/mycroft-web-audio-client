# Mycroft Web Client Experiment

this is a small web client experiment for [Mycroft](https://github.com/mycroftai/mycroft-core). It uses [recorder.js](https://github.com/mattdiamond/Recorderjs) and a simple flask application to perform the tasks.

The main thing this does is handle uploads of files and parses them, there is a web demo (currently only working in Firefox) where you can press and hold a button to record audio for Mycroft.


## Installing

This should be run on the same machine as the rest of the Mycroft stack.

Create a venv

`python3 -m venv venv`

Activate the venv

`source venv/bin/activate`

Install requirements

`pip install -r requirements.txt`

## Running

To lauch the flask app run

`flask run`

the service should now be available at http://localhost:5000

## Defined endoints
 - `/`
  - POST accepts files sent through forms
  - GET provides a simple form to test uploading files
 - /static/index.html
  - A simple interface for talking with Mycroft, accepts voice input and handles STT and passes the utterance to Mycroft Core
