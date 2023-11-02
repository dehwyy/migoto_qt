run:
	python3.11.exe src/main.py
gen:
	python3 gen.py
prod:
	pyinstaller src/main.py --noconsole --add-data "src/assets;assets" --icon="src/assets/icon.png" --name migotoqt --noconfirm && \
	cd dist/migotoqt && \
	md internal && cd internal && \
	md database

run-prod:
	cd dist/migotoqt && migotoqt.exe
