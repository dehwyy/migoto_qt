from os import listdir
import subprocess

# listdir returns both dirs and files, but in this case only files with ext .ui would exist
for file in listdir("./src/ui"):
    filename = file.split(".")[0]
    command = f"pyuic5.exe -x -o \
        ./src/internal/widgets/generated/{filename}UI.py ./src/ui/{file}"
    subprocess.run(command.split())

print("Generated .py files from .ui")
