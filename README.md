# Django Mentors
An application designed to aid in the matching of mentors and trainees, as well as uniting resources that help a new 
Django developer go above and beyond the usual resources available.

This application is viewable at https://djangomentors.com

## Development
Make an env.yml with your env vars in, e.g:

    ---
        
    ENV_VARS:
      DJANGO_SECRET_KEY: 'SOME_KEY'

## Local
- Build with `make local`
- Run with `./manage.py runserver`
- Test with `make test`

## Docker
- Build with `make docker-build`
- Run with `make docker-run` 

## Deployment
    make docker-deploy