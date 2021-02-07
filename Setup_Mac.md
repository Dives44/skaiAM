# Setup Mac
## 1. Remarques
* Dronekit a été construit sous python2. Ainsi, certains modules ainsi que certaines fonction
permettant d'automatiser les script python avec les commandes bash ne marchent pas sous python3.
La migration est toujours en cours..
* Il est donc nécéssaire d'utiliser python2.7 pour avoir un environnement entièrement fonctionnel
## 2. Installer l'environnement
### Repo Git
* Créer un compte GitHub:
* Installer Git
* Initialiser le repo Git:
    * cd chemin/voulu/vers/le/repo/git
    * git clone https://github.com/Dives44/skaiAM.git
    
### MacPorts
* Télécharger le code source adapté à votre version de MacOS ici https://github.com/macports/macports-base/releases/
(ne pas prendre les package en .asc)
* Double cliquer sur le package et faire un "easy install"
* Verifier que MacPorts est bien installé avec `$ port version` qui doit retourner `$ Version: x.x.x`

### IDE Pycharm
* Installer Pycharm: `$ sudo snap install pycharm-community --classic`
* Ouvrir le repo skaiAM avec 
* Créer un interpréteur python2.7 pour le projet et le lancer
> **ATTENTION**: A partir de cette étape les commandes bash devront être éxécutées dans 
le terminal Pycharm dans l'encironnement skaiAM - Pour vérifier ci c'est la cas toutes
les lignes du terminal doivent commencer par (skaiAM)

### Xcode

## 3.Installer les packages
* `$ sudo pip install numpy==1.16.6`
* `$ sudo pip install PyYAML==5.4.1`
* `$ sudo pip install lxml==4.6.2`
* `$ sudo pip install matplotlib==2.2.5`
* `$ sudo pip install opencv-python==4.2.0.32`
* `$ sudo pip install parsing==1.6.1`
* `$ sudo port install py27-serial`
* `$ sudo port install py27-wxpython-3.0`
* `$ sudo port install py27-pil`
* `$ sudo port install sqlite3-tcl`