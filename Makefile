SRC = poeditor/
TESTS = tests/

env:
	poetry install

fmt:
	isort ${SRC} ${TESTS}
	black ${SRC} ${TESTS}

lint:
	black --check ${SRC} ${TESTS}
	mypy ${SRC}

test:
	pytest ${TESTS}
