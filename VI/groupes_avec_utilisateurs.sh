#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 fichier_sortie"
    exit 1
fi

cut -d: -f1 /etc/group > "$1"

echo "Liste des groupes avec au moins un utilisateur écrite dans $1"
