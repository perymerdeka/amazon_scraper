build:

	docker compose -f docker-compose.yaml build --no-cache

upd:
	docker compose -f docker-compose.yaml up -d

up:
	docker compose -f docker-compose.yaml up

shell:
	docker compose -f docker-compose.yaml exec web bash

makemigrations:
	docker compose -f docker-compose.yaml exec web su -c "python manage.py makemigrations --settings=core.settings.production"

migrate:
	docker compose -f docker-compose.yaml exec web su -c "python manage.py migrate --settings=core.settings.production"

destroy:
	docker compose -f docker-compose.yaml down