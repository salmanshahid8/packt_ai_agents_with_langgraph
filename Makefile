sync:
	uv sync

format:
	uvx ruff format . --no-cache --respect-gitignore --quiet
# Replace --quiet with --verbose for detail

lint:
	uvx ruff check . --fix --no-cache --respect-gitignore --quiet --exit-zero
# Replace --quiet with --verbose for detail

type_check:
	uvx ty check --output-format 'concise' --quiet --exit-zero
# Replace --quiet with --verbose for detail

security_check:
	uvx bandit -r src/ --quiet --exit-zero
# Replace --quiet with --verbose for detail

build:
	uv build --clear --upgrade --quiet

clean:
	uvx ruff clean && uv clean

# test:
# 	python -m pytest -vv test_hello.py
	
all: sync format lint type_check security_check build clean