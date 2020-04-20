req:
	poetry export -f requirements.txt > requirements.txt --without-hashes

test:
	docker-compose run app sh -c 'python manage.py test && flake8'