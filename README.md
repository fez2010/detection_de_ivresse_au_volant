# Detection de l'ivresse au volant
Prédiction du risque de départ d'un employer a l'aide du dataset [turnover.csv](./datasets/DonneesTestSymptomatiqueDRE_A2012.xlsx) . Vous trouverez si join le [code source](./TP_MAP6009.ipynb) des expérimentations du [Rapport](./rappot/main.tex).

- [Description du dataset](#description-du-dataset)
- [Avant de Commencer le Travail](#avant-de-commencer-le-travail)
    - [Créer un environnement virtuel python](#creer-un-environnement-virtuel-pythoncreer-)
    - [Lancer L'environnement Python](#lancer-lenvironnement-python)
    - [Installer jupyter et jupyter kernel](#installer-jupyter-et-jupyter-kernel)
    - [Créer et installer un nouveau kernel jupyter](#creer-et-installer-un-nouveau-kernel-jupyter)
- [Lancer le code source](#lancer-le-code-source)
- [Resultats obtenus](#resultats-obtenus)
- [Références](#references)
## Description du dataset

## Avant de Commencer le Travail
### Créer un environnement virtuel python
`conda create --name ivre_dec python=3.8`
### Lancer L'environnement Python 
`conda activate ivre_dec`
### Installer jupyter et jupyter kernel
```
conda install jupyter
conda install ipython
conda install ipykernel
pip install bash_kernel
```
### Créer et installer un nouveau kernel jupyter 
```
ipython kernel install --user --name=ivre_dec
python -m ipykernel install --user --name=ivre_dec
python -m bash_kernel.install
```
### Installation des polices de caracteres suivant votre system
#### Ubuntu  
`sh setup/ubuntu/font_setup.sh`
#### Mac os
`sh setup/macos/font_setup.sh` 
## Lancer le serveur des logs
`Make experiments`
## Lancer le code source
`Make open`
## Resultats obtenus
## Avant le build
`Make dep`
## Build
Vous pouvez build le model, pdf...
`Make build`
## Références
* [venv installations and kernel creation](https://medium.com/@WamiqRaza/how-to-create-virtual-environment-jupyter-kernel-python-6836b50f4bf4)
* [Theme](./theme/AdobeColor-My%20Color%20Theme-3.jpeg)
* [Latex](https://guides.nyu.edu/LaTeX/installation)