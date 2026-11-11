
# Reconnaissance de la langue des signes avec Deep Learning

## 1. Présentation du projet

Ce projet consiste à développer un système intelligent capable de reconnaître les lettres de l'alphabet en langue des signes américaine (ASL) à partir d'images de gestes de la main.

Pour réaliser cette tâche, nous utilisons des techniques de Deep Learning, notamment les réseaux de neurones convolutifs (CNN — Convolutional Neural Networks).

Le modèle est entraîné sur le dataset **Sign Language MNIST**, qui contient des images représentant différentes lettres de l'alphabet en langue des signes.

Après la phase d'entraînement, le modèle est utilisé dans une application de reconnaissance en temps réel à l'aide d'une webcam.

## 2. Objectifs du projet

Les principaux objectifs sont :

- Comprendre et appliquer les concepts fondamentaux du Deep Learning.
- Préparer et traiter un dataset d'images.
- Concevoir et entraîner un réseau de neurones convolutif (CNN).
- Évaluer les performances du modèle de classification.
- Sauvegarder et réutiliser le modèle entraîné.
- Développer un système de reconnaissance des gestes en temps réel avec OpenCV.

## 3. Dataset : Sign Language MNIST

Le projet utilise le dataset **Sign Language MNIST**, conçu pour la reconnaissance des lettres de l'alphabet en langue des signes américaine (ASL).

Le dataset contient des images en niveaux de gris représentant des positions de la main. Chaque image possède une étiquette correspondant à une lettre.

### 3.1 Organisation des données

Deux fichiers CSV sont utilisés :

| Fichier | Description |
|---|---|
| `sign_mnist_train.csv` | Données utilisées pour entraîner le modèle |
| `sign_mnist_test.csv` | Données utilisées pour tester le modèle |

### 3.2 Caractéristiques des images

- Dimensions : 28 × 28 pixels.
- Format : niveaux de gris.
- Nombre de classes : 24 lettres.
- Valeurs des pixels : de 0 à 255.
- La lettre J et la lettre Z sont exclues du dataset, car elles nécessitent un mouvement de la main.

### 3.3 Organisation dans le projet

Les fichiers sont conservés dans le dossier :

```text
data/
└── raw/
    ├── sign_mnist_train.csv
    └── sign_mnist_test.csv
```

## 4. Prétraitement des données

Avant d'entraîner le réseau de neurones convolutif, les données doivent être préparées afin de faciliter l'apprentissage du modèle.

Les étapes de prétraitement comprennent :

### 4.1 Séparation des caractéristiques et des étiquettes

Chaque ligne du dataset contient :
- Une étiquette (`label`) qui représente la lettre à reconnaître.
- 784 valeurs correspondant aux pixels de l'image (28 × 28).

Les étiquettes sont séparées des pixels afin de préparer les données pour la classification.

### 4.2 Redimensionnement des images

Les 784 valeurs de pixels sont réorganisées sous forme d'images de dimensions 28 × 28 pixels.

### 4.3 Normalisation

Les valeurs des pixels, initialement comprises entre 0 et 255, sont normalisées entre 0 et 1.

Cette opération permet de faciliter et de stabiliser l'apprentissage du réseau.

La normalisation est réalisée avec la formule :

\[
X_{\text{normalisé}} = \frac{X}{255}
\]

### 4.4 Ajout de la dimension des canaux

Une dimension supplémentaire est ajoutée pour représenter le canal de couleur.

Chaque image est ainsi représentée sous la forme :

```text
28 × 28 × 1
```

Le chiffre 1 correspond au canal unique des images en niveaux de gris.
