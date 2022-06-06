# flask-sandbox

## Activate Virtual Environment
`source replace_with_virtualenv_name_here/bin/activate`

## Flask Setup
- `export FLASK_APP=run`
- `export FLASK_CONFIG=development`

## Run Application
- `flask run`

## Update Requirements and Create lib folder
- `pip install -t lib -r requirements.txt`

## Freeze requirements to file
- `pip freeze > requirements.txt`

## Flask DB Commands

- Initialize Migrations - One Time Setup
`flask db init`

- Create Migration Script
`flask db migrate -m 'comment-here'`

- Run Migration Script
`flask db upgrade`

## Testing Entries
- `python3 -m unittest -v tests.py`