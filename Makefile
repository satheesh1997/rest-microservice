IMAGE_NAME = "satheesh1997/rest-microservice"

requirements:
	pip install pipenv
	pipenv install
	pipenv lock -r > requirements.txt

image:
	docker build -t ${IMAGE_NAME} .
