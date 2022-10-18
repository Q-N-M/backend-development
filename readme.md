
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
