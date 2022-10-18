
## Table of Contents

- [Local Configuration](#local-configuration)
- [Deployed API URLs](#deployed-api-urls)

## Local Configuration

- Install Python 3.6 or higher and PostgreSQL
- Create Python virtual environment and install requirements
  ```bash
  $ cd /path/to/project/directory
  $ python3 -m venv env
  $ source env/bin/activate
  $ pip3 install -r requirements.txt
  ```
  - Set up environment variables (change as needed)
  ```bash
  $ export DATABASE_HOST='127.0.0.1'
  $ export DATABASE_NAME='wellderly'
  $ export DATABASE_PASSWORD='postgres'
  $ export DATABASE_PORT='5432'
  $ export DATABASE_USER='postgres'
  $ export DJANGO_SETTINGS_MODULE='wellderly.settings.local'
  $ export SECRET_KEY='7&s33ax$lxxzti1)0y=8#tu!$7bdy)p$1@kn06tp&8x8i9#h2u'
  ```
- Migrate the database
  ```bash
  $ python3 manage.py migrate
  ```
- Create Superuser
  ```bash
  $ python3 manage.py createsuperuser
  ```
- Run server
  ```bash
  $ python3 manage.py runserver
  ```

## Deployed API URLs

- API List: [https://backend-deco.herokuapp.com/api/v1/](https://backend-deco.herokuapp.com/api/v1/)
- User Emoji: [https://backend-deco.herokuapp.com/api/v1/user-emoji/](https://backend-deco.herokuapp.com/api/v1/user-emoji/)
- User Analysis: [https://backend-deco.herokuapp.com/api/v1/user-analysis/](https://backend-deco.herokuapp.com/api/v1/user-analysis/)
