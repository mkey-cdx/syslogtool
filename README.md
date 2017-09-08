# syslogtool
Cet outil s'appuie sur un socket python pour mettre à disposition le fichier syslog, sur requête d'un client.<br/>
Le serveur attend une requete ['GET_LOG'] du client pour copier le fichier dans /var/tmp/. Une fois le fichier copié, le serveur notifie le client ['OK'], qui pourra lancer le téléchargement avec rsync. Une réponse ['KO'] est envoyée si le fichier n'est pas trouvé.<br/>
Lorsque le téléchargement est terminé, le client notifie le serveur ['OK'], qui pourra alors nettoyer le répertoire de travail temporaire.<br/>
L'utilisation de rsync permet de compresser l'envoi du fichier au travers du réseau et d'appuie sur SSH pour chiffrer la communication.

## Installation
- Placer les fichiers *server.py* et *server.ini* sur le serveur.<br/>
- Placer les fichiers *client.py* et *client.ini* sur le poste client.<br/>
- Générer un certificat ssh pour l'utilisateur qui exécutera client.py et ajouter la clé publique dans le fichier *.ssh/authorized_keys* du serveur.<br/>

## Configuration
La configuration des composants s'effectue au sein des fichiers *server.ini* et *client.ini*.

## Exécution
Sur le serveur, exécuter le fichier *server.py*.<br/>
Sur le poste client, exécuter le fichier *client.py*.<br/>
Le fichier téléchargé sera placé dans le répertoire courant.
