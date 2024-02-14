import subprocess

# Afficher le contenu du répertoire /home
print("Contenu du répertoire /home :")
subprocess.run(["ls", "/home"])

# Afficher le nom et le groupe de l'utilisateur qui lance le script
print("Nom de l'utilisateur :", subprocess.run(["whoami"], capture_output=True, text=True).stdout.strip())
print("Groupe de l'utilisateur :", subprocess.run(["id", "-gn"], capture_output=True, text=True).stdout.strip())
