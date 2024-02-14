import sys

if len(sys.argv) < 2:
    print("Usage: python script.py nom_du_fichier")
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    lines.sort()

for line in lines:
    print(line.strip())