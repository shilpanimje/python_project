# Add any tasks that are not dependent on files to the .PHONY list.
.PHONY: dev test lint pip_dev

dev:
    python dev.py

test:
    py.test tests/ --cov python_crud --cov-report term-missing

lint:
    flake8 python_crud/ tests/

pip_dev:
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
