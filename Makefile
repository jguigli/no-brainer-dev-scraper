.PHONY: all build up logs exec_scraper

all:
	docker-compose up --build -d

build:
	docker-compose build

up:
	docker-compose up -d

logs:
	docker-compose logs -f scraper

exec_scraper:
	docker exec -it dev_scraper bash
