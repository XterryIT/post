migrate:
	docker compose exec web python manage.py makemigrations
	docker compose exec web python manage.py migrate

up:
	docker compose build
	docker compose up 

.PHONY: up migrate