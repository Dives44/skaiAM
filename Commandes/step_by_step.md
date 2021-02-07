# Step By Step - Commandes

## Principe
* Ardupilot permet d'envoyer des commande "prémachées" (Mavlink) au drone à partir du Terminal.
Cependant ces commandes doivent etre envoyées une par une et ne sont pas adapté à une
adaptation en temps réel du drone à son environnement. C'est pour cela que Dronekit a
été créé, pour automatiser avec Python l'envois de commandes Mavlink.
* L'utilisation directe de Ardupilot n'est donc pas obligatoire mais permet de comprendre
le fonctionnement des pararètres, du protocol MAVlink etc.. qui sont assez utiles pour débuguer.

##Les étapes
1. Installer Ardupilot
2. Lancer pour la première fois SITL
3. Connecter MAVProxy et QGControl à un drone simulé avec SITL
4. Afficher les paramètres du drone et les modifier
5. Installer Dronekit
6. Lancer un véhicule simulé avec dronekit et le connecter à QGControl
7. Lancer un simple_takeoff
8. Créer une mission la télécharger avec Dronekit pour la lancer