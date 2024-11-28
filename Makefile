BIN ?= .venv/bin/

CODE = quicks
ALL_CODE = quicks tests

.PHONY: test
test:
	$(BIN)pytest --verbosity=2 --showlocals --strict --log-level=DEBUG --cov=$(CODE) $(args)

.PHONY: lint
lint:
	$(BIN)ruff check $(ALL_CODE)
	$(BIN)pytest --dead-fixtures --dup-fixtures
	$(BIN)mypy $(ALL_CODE)

.PHONY: format
format:
	$(BIN)ruff format $(ALL_CODE)

.PHONY: run
run:
	rm -r simple-project || true
	python -m quicks example.yml simple-project
