To run from the command line, do the following from the project root:
```
$ python -m venv venv
$ . venv/bin/activate
$ pip install -e .
$ pip install flask
$ export FLASK_APP=url_check.py
$ export FLASK_ENV=development  # for debugging
$ flask init-db
$ flask run
```

The FLASK_ENV variable above is optional but it will dump a stack trace to the
browser if there is some kind of server error.

You can import the test data into the database by doing
```
$ sqlite3 instance/url_check.sqlite < tests/data.sql
```
You can import custom data in a similar way.

It's probably best to test with [Postman](https://www.postman.com/downloads/)
since there's no body returned in the response.  It won't be possible to detect
if it's working with a normal browser.
