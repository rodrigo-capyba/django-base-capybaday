ARG := $(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))
$(eval $(ARG):;@true)

perms:
	sudo chown -hR ${USER}:${USER} .

build:
	docker-compose build

up:
	docker-compose up

enter:
	docker-compose exec $(ARG) bash

setup_install:
	bash scripts/setup-install.sh

setup_venv:
	bash scripts/setup-venv.sh

startapp:
	bash scripts/start-app.sh $(ARG)

run:
	bash scripts/docker-run.sh $(ARG)

migrations:
	bash scripts/docker-run.sh python manage.py makemigrations $(ARG)

migrate:
	bash scripts/docker-run.sh python manage.py migrate

seed:
	bash scripts/docker-run.sh python manage.py runscript seed

reset_schema:
	bash scripts/docker-run.sh python manage.py reset_schema

shell:
	bash scripts/docker-run.sh python manage.py shell

test:
	bash scripts/docker-run.sh pytest

test_create_db:
	bash scripts/docker-run.sh pytest --create-db

total_reset: reset_schema migrate seed
