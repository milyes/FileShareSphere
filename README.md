# FileShareSphere

Plateforme simple pour le partage de fichiers via Flask.

## Utilisation

1. Lancer l'application :
```bash
python app.py
```

2. Envoyer un fichier :
```bash
curl -F "file=@monfichier.txt" http://localhost:5000/upload
```

3. Télécharger un fichier :
```bash
http://localhost:5000/download/monfichier.txt
```