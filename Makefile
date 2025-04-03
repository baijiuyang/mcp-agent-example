install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install black flake8 pipreqs

format:
	black .

lint:
	flake8 .

deps:
	pipreqs --savepath requirements.txt .

host:
	uvicorn main:app --port 8000 --reload

run:
	python openai_agent.py

test-api:
	python test_api.py