collectstatic:
	python3 django_site/manage.py collectstatic

migrations:
	python3 django_site/manage.py makemigrations

migrate:
	python3 django_site/manage.py migrate

run-server:
	python3 django_site/manage.py runserver
	

watch:
	sass --watch frontend/scss/custom.scss frontend/css/custom.css

check-deploy:
	python3 django_site/manage.py check --deploy


run-production-server:
	cd django_site/ && gunicorn django_site.mysite.wsgi:application


install:
	poetry install

update: migrate collectstatic ;