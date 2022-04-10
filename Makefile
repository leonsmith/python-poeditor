env:
	poetry install

fmt:
	black poeditor/

lint:
	black --check poeditor/

test:
	pytest tests/
