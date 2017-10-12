registry = "036427539303.dkr.ecr.eu-west-1.amazonaws.com"

# Make a virtual environment with python 3, install deps and migrate the db (sqlite locally)
local:
	python3.6 -m venv .venv
	. .venv/bin/activate
	pip3 install -r requirements.txt
	./manage.py migrate

test:
	./manage.py test

docker-build:
	docker build -t farridav/django-mentors .

docker-run:
	docker run --rm -it -p 8000:8000 farridav/django-mentors

docker-debug:
	docker run --rm -it farridav/django-mentors /bin/sh

docker-auth:
	aws ecr get-login --no-include-email --region eu-west-1

docker-deploy:
	docker tag farridav/django-mentors:latest $(registry)/farridav/django-mentors:latest
	docker push $(registry)/farridav/django-mentors:latest