=======
Cropper
=======
URL shortener API example in Django.

Setup
-----
- Clone, configure virtual environment, run: ::

    $ git clone git@github.com:kylepw/cropper.git
    $ cd cropper && python3 -m venv venv && source venv/bin/activate && python3 install -r requirements.txt
    $ echo SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')" > .env
    $ python3 manage.py runserver

Usage
-----
- List: ::

    curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/v1/

- Redirect (or use web browser): ::

    curl -L http://127.0.0.1:8000/v1/kmdzuw

- Create: ::

    curl -X POST http://127.0.0.1:8000/v1/   \
         -H 'Content-Type: application/json' \
         -d '{"url":"https://www.wfmu.org/recentarchives.php"}'

- Run tests (from top of repo): ::

    python3 manage.py test

- Test coverage (from top of repo): ::
  
    coverage run manage.py test
    coverage report

The Meat
--------
Files of interest: ::

    cropper/views.py
    cropper/serializers.py
    cropper/utils.py
    cropper/tests