# Memory_game_POO

## Description
Ce projet est une implémentation du jeu de Simon sur une **Raspberry Pi Pico**. Le but du jeu est de reproduire une séquence lumineuse qui s'allonge progressivement. L'utilisateur doit entrer la bonne séquence en utilisant les touches **1 (Rouge), 2 (Jaune), 3 (Bleu)**.

## Fonctionnalités
- Affichage d'une séquence aléatoire de LEDs.
- Saisie utilisateur pour reproduire la séquence.
- Vérification des entrées avec message d'erreur en cas de mauvaise réponse.
- Ajout d'une nouvelle LED à la séquence après chaque réussite.
- Pause de 1 seconde après avoir complété une séquence avant d'ajouter la suivante.

## Matériel Requis
- **Raspberry Pi Pico**
- **Breadboard**
- **3 LEDs (Rouge, Jaune, Bleue)**
- **3 résistances (330Ω)**
- **Câbles de connexion**

## Installation
1. **Installer MicroPython sur la Raspberry Pi Pico** (si ce n'est pas déjà fait).
2. **Utiliser Thonny** ou un autre éditeur MicroPython.
3. **Copier le fichier `simon.py`** dans la Pico.
4. **Exécuter le script.**

## Utilisation
1. **Regardez la séquence affichée par les LEDs.**
2. **Entrez la séquence en appuyant sur les touches 1, 2, 3.**
3. **Si vous réussissez, la séquence s'allonge !**
4. **Si vous faites une erreur, le jeu s'arrête.**


## Améliorations Possibles
- Ajouter du son lorsque la LED s'allume.
- Afficher le score sur un écran LCD ou un affichage 7 segments.
- Ajouter une difficulté croissante avec un temps limité pour répondre.

## Auteur
**[Nicolas SUNG]** - Développement & Documentation
