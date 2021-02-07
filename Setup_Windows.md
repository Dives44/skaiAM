# Setup Windows
* Windows n'utilise pas un terminal bash comme MacOS et les distributions linux. Or le drone utilise bash pour automatiser
les scripts python. De plus, certains packages (nottement MavProxy) ont des problèmes de compatibilités sous windows. Il est donc fortement recommandé
pour tout utilisateurs de Windows n'ayant pas de dual boot d'utiliser une machine virtuel.
Il vous suffit de suivre le tutoriel ici:http://doc.ubuntu-fr.org/virtualbox puis de suivre la procédure linux dans Setup_Linux.md.
* Il est forttement recommandé d'installé la distribution 16.04 et non 20.04 pour ne pas avoir à créer d'environnement python virtuel.
* ATTENTION: avant de lancer l'installation lisez entièrement Setup_Linux.md
## Station de controle
> Même si la simulation doit tourner sous linux, il est tout à fait possible de lancer QGControl sous Windows pour avoir
 en fenétré d'un coté la station de control et de l'autre Linux (c'est même recommandé pour des quesion de performance)
 * Il suffit de télécharger le fihier .exe: https://s3-us-west-2.amazonaws.com/qgroundcontrol/latest/QGroundControl-installer.exe
 * Puis de le lancer