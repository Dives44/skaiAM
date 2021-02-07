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
    * cd chemin/voulu/vers/le/repo/git
    * git clone https://github.com/Dives44/skaiAM.git

###QGroundControl
> C'est la station de controle
* Entrer dans le terminal
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