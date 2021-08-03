=======
Cropper
=======
URL shortener API example in Django.

Setup
-----
- Clone, configure virtual environment, migrate, run: ::

    git clone git@github.com:kylepw/cropper.git && \
    cd cropper && python3 -m venv venv && source venv/bin/activate && pip3 install -U pip -r requirements.txt && \
    echo SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')" > .env && \
    python3 manage.py migrate && python3 manage.py loaddata db.json && \
    python3 manage.py runserver

Usage
-----
- List: ::

    curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/v1/

- Redirect (or use web browser): ::

    curl -L http://127.0.0.1:8000/v1/s63vcj

- Create: ::

    curl -X POST http://127.0.0.1:8000/v1/   \
         -H 'Content-Type: application/json' \
         -d '{"url":"https://www.gmail.com"}'

- Run tests (from top of repo): ::

    python3 manage.py test

- Test coverage (from top of repo): ::
  
    coverage run manage.py test && coverage report

The Meat
--------
Files of interest: ::

    cropperapi/views.py
    cropperapi/serializers.py
    cropperapi/models.py
    cropperapi/utils.py
    cropperapi/tests