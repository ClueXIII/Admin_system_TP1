import subprocess

subprocess.run("touch tmp/fichier1 tmp/fichier2", shell=True)
subprocess.run("chmod 750 tmp/fichier1 tmp/fichier2", shell=True)