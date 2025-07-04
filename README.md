## 🚗 Car Data ETL Project

Ce projet Python effectue un processus **ETL (Extract – Transform – Load)** sur des fichiers de données contenant des informations sur des véhicules. Il récupère automatiquement les fichiers de formats différents (CSV, JSON, XML), les fusionne, transforme certaines valeurs, puis les sauvegarde dans un fichier CSV unique.

### 🎯 Objectif

* Extraire des données provenant de fichiers `*.csv`, `*.json`, et `*.xml` du répertoire.
* Convertir les prix des voitures d’**inches** en **mètres** (logique d'exemple).
* Enregistrer les données transformées dans un fichier unique `transformed_data.csv`.
* Journaliser chaque étape dans un fichier `log_file.txt`.

### 🧱 Structure du projet

```text
├── extract_transform_load.py     # Script principal ETL
├── transformed_data.csv          # Résultat final consolidé
├── log_file.txt                  # Journal du processus
├── fichier1.csv / .json / .xml   # Fichiers source (non fournis ici)
├── README.md                     # Documentation
```

### 📁 Champs attendus dans les fichiers

Tous les fichiers doivent contenir ces colonnes (ou balises) :

* `car_model` : modèle de la voiture
* `year_of_manufacture` : année de fabrication
* `price` : prix (à convertir)
* `fuel` : type de carburant

### 🧪 Traitement appliqué

| Étape         | Détail                                                              |
| ------------- | ------------------------------------------------------------------- |
| **Extract**   | Lit tous les fichiers `.csv`, `.json`, et `.xml` du répertoire.     |
| **Transform** | Multiplie la colonne `price` par `0.0254` pour convertir en mètres. |
| **Load**      | Sauvegarde les données dans `transformed_data.csv`.                 |
| **Log**       | Chaque étape est journalisée dans `log_file.txt`.                   |


### 🛠️ Technologies utilisées

* Python 3.x
* [pandas](https://pandas.pydata.org/)
* [glob](https://docs.python.org/3/library/glob.html)
* [xml.etree.ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html)
* [datetime](https://docs.python.org/3/library/datetime.html)

### ✅ Instructions d'exécution

1. Placez vos fichiers `.csv`, `.json`, et `.xml` dans le même dossier que le script.
2. Installez les dépendances si nécessaire :

```bash
pip install pandas
```

3. Lancez le script :

```bash
python extract_transform_load.py
```

4. Résultat :

   * `transformed_data.csv` contiendra les données fusionnées et converties.
   * `log_file.txt` contiendra les logs d’exécution avec horodatage.

### 📌 Exemple de log (`log_file.txt`)

```
2025-Jun-24-11:00:00,ETL Job Started
2025-Jun-24-11:00:01,Extract phase Started
2025-Jun-24-11:00:03,Extract phase Ended
2025-Jun-24-11:00:04,Transform phase Started
2025-Jun-24-11:00:05,Transform phase Ended
2025-Jun-24-11:00:06,Load phase Started
2025-Jun-24-11:00:07,Load phase Ended
2025-Jun-24-11:00:07,ETL Job Ended
```

### 🔎 Remarques

* Le fichier `transformed_data.csv` est ignoré à l’extraction pour éviter les boucles infinies.
* Le traitement suppose que le champ `price` est une mesure en inches (exemple fictif), ce qui peut être remplacé par une logique réelle selon vos données.
* Le script peut facilement être modifié pour charger les données vers une base SQL ou un service cloud.
