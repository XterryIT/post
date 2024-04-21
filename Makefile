migrate:
	docker compose exec web python manage.py makemigrations
	docker compose exec web python manage.py migrate

server:
	docker compose build

up:
	docker-compose up 

.PHONY: up server migrate