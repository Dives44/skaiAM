# Setup Windows
* Windows n'utilise pas un terminal bash comme MacOS et les distributions linux. Or le drone utilise bash pour automatiser
les scripts python. De plus, certains packages (nottement MavProxy) ont des problèmes de compatibilités sous windows. Il est donc fortement recommandé
pour tout utilisateurs de Windows n'ayant pas de dual boot d'utiliser une machine virtuel.
Il vous suffit de suivre le tutoriel ici:http://doc.ubuntu-fr.org/virtualbox puis de suivre la procédure linux dans Setup_Linux.md.
* Il est forttement recommandé d'installé la distribution 16.04 et non 20.04 pour ne pas avoir à créer d'environnement python virtuel.
* ATTENTION: avant de lancer l'installation lisez entièrement Setup_Linux.md