# 📰 New Nork Nimes

#### Nll Nhe News Nhat's Nit No Nrint

New Nork Nimes searches nytimes.com for all headlines in a given year and month, and returns a list of all two-word alliterations ("nimes") used in the headlines. New Nork Nimes is a [Flask](https://flask.palletsprojects.com/en/3.0.x/) app, using [Bootstrap](https://getbootstrap.com/) for styling. 

You can sometimes see a running example at https://useful-molly-intimate.ngrok-free.app.

## Installing
New Nork Nimes runs on Python 3.10. 

Clone the repo and change to its directory.

```
$ git clone https://github.com/lesservehicle/newnorknimes.git
$ cd newnorknimes
```

Get [pyenv](https://github.com/pyenv/pyenv). Install the latest version of 3.10.

```bash
$ pyenv install 3.10.13
```

Get [pipenv](https://pipenv.pypa.io/en/latest/), too. Make a virtual environment for New Nork Nimes.

```bash
$ pipenv install --python=3.10
```

Activate the virtual environment.

```bash
$ pipenv shell
```

Pipenv should have installed all of the requirements from the Pipfile, but if it didn't, you can tell it to try again.
```bash
$ pipenv install -r requirements.txt
```

## Running
New Nork Nimes only runs in development mode at the moment. Tell flask to run it.

```bash
flask --app nimes_app.webapp run
 * Serving Flask app 'nimes_app.webapp'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Open your browser to http://127.0.0.1:5000. Enjoy New Nork Nimes.

## To Do
- Load data into Pandas DataFrame for more analysis and outputs
- Make it look a little nicer
- Instructions for deploying with UWSGI
- Instructions for deploying with ngrok
- Ability to visually create refridgerator magnet poetry by selecting different nimes in a given month

&copy; 2023 Big Fire LLC