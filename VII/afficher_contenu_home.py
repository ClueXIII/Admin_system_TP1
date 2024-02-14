import os

# Afficher le contenu du répertoire /home
print("Contenu du répertoire /home :")
for file in os.listdir("/home"):
    print(file)

# Afficher le nom de l'utilisateur actuel en utilisant la variable d'environnement USER
user = os.environ.get('USER')
if user:
    print("Nom de l'utilisateur :", user)
    print("Id groupe de l'utilisateur :", os.getegid())
else:
    print("Impossible de déterminer le nom de l'utilisateur.")

# Afficher le nom du groupe de l'utilisateur actuel

