setup-venv:
	source .venv/bin/activate

run:
	python3.11.exe src/main.py

gen:
	python3 gen.py

update-deps:
	python3 -m pip freeze > requirements.txt
