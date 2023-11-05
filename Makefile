run:
	cd src && python3.11.exe main.py
prod:
	pyinstaller src/main.py --noconsole --add-data "src/assets;assets" --icon="src/assets/icon.png" --name migotoqt --noconfirm && \
