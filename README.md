# Django Mentors
An application designed to aid in the matching of mentors and trainees, as well as uniting resources that help a new 
Django developer go above and beyond the usual resources available.

This application is viewable at https://djangomentors.com

## Development
Make an env.yml with your env vars in, e.g:

    ---
        
    ENV_VARS:
      DJANGO_SECRET_KEY: 'SOME_KEY'

### Build
Make a virtual environment with python 3, install deps and migrate the db (sqlite locally)

    python3.6 -m venv .venv && . .venv/bin/activate
    pip3 install -r requirements.txt
    ./manage.py migrate

### Run
    ./manage.py runserver
### Test
    ./manage.py test

## Docker

### Build    
    docker build -t farridav/django-mentors .

### Run
    docker run --rm -it -p 8000:8000 farridav/django-mentors
    
## Deployment
TODO