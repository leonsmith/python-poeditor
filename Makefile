env:
	poetry install

fmt:
	black poeditor/ tests/

lint:
	black --check poeditor/ tests/

test:
	pytest tests/
