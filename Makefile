req:
	poetry export -f requirements.txt > requirements.txt --without-hashes

test:
	docker-compose run --rm app sh -c 'python manage.py test && flake8'

migrations:
	docker-compose run app sh -c 'python manage.py makemigrations'
