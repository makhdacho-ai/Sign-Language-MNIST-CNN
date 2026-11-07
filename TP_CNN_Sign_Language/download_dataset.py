import kagglehub
import shutil
from pathlib import Path

# Télécharger le dataset depuis Kaggle
print("Téléchargement du dataset...")

download_path = kagglehub.dataset_download(
    "datamunge/sign-language-mnist"
)

# Chemins du projet
project_dir = Path(__file__).resolve().parent
data_dir = project_dir / "data"

# Créer le dossier data s'il n'existe pas
data_dir.mkdir(exist_ok=True)

# Copier les deux fichiers CSV
files = [
    "sign_mnist_train.csv",
    "sign_mnist_test.csv"
]

for filename in files:
    source = Path(download_path) / filename
    destination = data_dir / filename

    shutil.copy2(source, destination)
    print(f"Fichier copié : {destination}")

print("\nTéléchargement terminé !")