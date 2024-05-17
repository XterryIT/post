migrate:
	docker compose exec web python manage.py makemigrations
	docker compose exec web python manage.py migrate

freeze:
	pip freeze > requirements.txt

up:
	docker compose build
	docker compose up 

drop:
	docker compose exec web python manage.py migrate crm zero

.PHONY: up migrate freeze