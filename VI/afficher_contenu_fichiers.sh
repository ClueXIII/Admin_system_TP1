#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 fichier1 fichier2 ..."
    exit 1
fi

for file in "$@"; do
    if [ -f "$file" ]; then
        echo "Contenu de $file :"
        cat "$file"
        echo ""
    else
        echo "Le fichier $file n'existe pas."
    fi
done

#./afficher_contenu_fichiers.sh fichier1 fichier2 ...