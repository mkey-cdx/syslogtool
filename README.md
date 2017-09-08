# syslogtool
Cet outil s'appuie sur un socket python pour mettre à disposition le fichier syslog, sur requête d'un client.

## Installation
Placer les fichiers server.py et server.ini sur le serveur.
Placer les fichiers client.py et client.ini sur le poste client.
Générer un certificat ssh pour l'utilisateur qui exécutera client.py et ajouter la clé publique dans le fichier .ssh/authorized_keys du serveur.

## Configuration
La configuration des composants s'effectue au sein des fichiers server.ini et client.ini.

## Exécution
Sur le serveur, exécuter le fichier server.py.
Sur le poste client, exécuter le fichier client.py.
