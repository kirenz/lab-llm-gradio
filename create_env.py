from pathlib import Path
import subprocess

# Setze den Pfad zum Zielordner
target_folder = Path("slides/env")

# Erstelle den Ordner, falls er noch nicht existiert
target_folder.mkdir(parents=True, exist_ok=True)

# Wechseln in den Ordner 'slides' und führen den 'conda' Befehl aus
command = f"cd {target_folder.parent} && conda create --prefix env python"

# Führen den Befehl im Terminal aus
subprocess.run(command, shell=True)


####################################
# Nächste Schritte

# Anaconda activate in Terminal
# conda activate ./env

# Installation der Module

# Export yml
# conda env export > environment.yml

# Restore env
# conda env create --prefix env -f environment.yml
