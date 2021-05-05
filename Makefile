all: requirements run

requirements:
	pip install -r requirements.txt

run:
	python3 main.py
