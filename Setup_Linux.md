# Setup Linux
## 1. Remarques
* Dronekit a été construit sous python2. Ainsi, certains modules ainsi que certaines fonction
permettant d'automatiser les script python avec les commandes bash ne marchent pas sous python3.
La migration est toujours en cours..
* Il est donc nécéssaire d'utiliser python2.7 pour avoir un environnement entièrement fonctionnel
## 2. Installer l'environnement
> A partir d'Ubuntu 20.04 python3 est la version par défaut. Il faut donc bien faire attention à
installer un environnement virtuel avec python2.7

Pour connaitre la version de python il faut executer `$ python --version` 
### Repo Git
* Créer un compte GitHub:
* Installer Git
* Initialiser le repo Git:
 >
    $ cd chemin/voulu/vers/le/repo/git
    $ git clone https://github.com/Dives44/skaiAM.git
* Il est recommandé d'installer aussi GitHub Desktop pour se simplifier encore plus la vie
https://desktop.github.com

### Ardupilot
> Installer Ardupilot dans un répertoire autre que le repository Git
>
    $ git clone -b Copter-3.5.5 https://github.com/ardupilot/ardupilot
    $ cd ardupilot/
    $ git submodule update --init --recursive
    $ cd Tools/autotest/
    $ pwd (Copier le résultat de cette commande)
    $ sudo vi ~/bashrc
* Ajouter à la fin (en apuyant sur I pour insert)
>
    $ export PATH="resulat/de/la/commande/copiée/plius/haut":$PATH
* Apuyer sur Echap puis taper wq et Entrer
* Cela permet de ne pas avoir à retourner dans les fichier Ardupilot à chaque fois pour le lancer. Après ces
lignes de commandes il sera possible de lancer depuis n'importe quel répertoire Ardupilot
>
    $ source ~/.bashrc
    

### QGroundControl
> C'est la station de controle
>
    $ sudo usermod -a -G dialout $USER
    $ sudo apt-get remove modemmanager -y
    $ sudo apt install gstreamer1.0-plugins-bad gstreamer1.0-libav gstreamer1.0-gl -y
* Se déconnecter puis se reconnecter
* Télécharger https://s3-us-west-2.amazonaws.com/qgroundcontrol/latest/QGroundControl.AppImage
* Installer
>   
    $ chmod +x ./QGroundControl.AppImage
* Lancer
>
    $ ./QGroundControl.AppImage

### MAVProxy
> C'est la station de controle en ligne de commandes
>
    $ sudo apt-get install python-dev python-opencv python-wxgtk4.0 python-pip python-matplotlib python-lxml python-pygame
    $ pip install PyYAML mavproxy --user
    $ echo "export PATH=$PATH:$HOME/.local/bin" >> ~/.bashrc
S'il y a une erreur "permission denied" il changer les droits de l'utilisateurs
>
    $ sudo usermod -a -G dialout <username>
Mettre à jour
>
    $ pip install mavproxy --user --upgrade


### IDE Pycharm
* Installer Pycharm: 
>
    $ sudo snap install pycharm-community --classic
* Ouvrir le repo skaiAM avec 
* Créer un interpréteur python2.7 pour le projet et le lancer
> **ATTENTION**: A partir de cette étape les commandes bash devront être éxécutées dans 
le terminal Pycharm dans l'encironnement skaiAM - Pour vérifier ci c'est la cas toutes
les lignes du terminal doivent commencer par (skaiAM)

## 3.Installer les packages
> En cours d'usinage
>
    $ sudo pip install numpy==1.16.6
    $ sudo pip install PyYAML==5.4.1
    $ sudo pip install lxml==4.6.2
    $ sudo pip install matplotlib==2.2.5
    $ sudo pip install opencv-python==4.2.0.32
    $ sudo pip install parsing==1.6.1
    $ sudo port install py27-serial
    $ sudo port install py27-wxpython-3.0
    $ sudo port install py27-pil
    $ sudo port install sqlite3-tcl