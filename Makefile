docker-build:
	docker build -t farridav/django-mentors .

docker-run:
	docker run --rm -it -p 8000:8000 farridav/django-mentors

docker-debug:
	docker run --rm -it farridav/django-mentors /bin/sh