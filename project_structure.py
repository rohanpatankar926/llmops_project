import os

def create_folder_structure():
    base_folder = "backend/app"
    
    folders = [
        "Infra",
        "k8s",
    ]
    
    for folder in folders:
        folder_path = os.path.join(base_folder, folder)
        os.makedirs(folder_path, exist_ok=True)

    files = [
        "Dockerfile",
        "Infra/main.tf",
        "Infra/output.tf",
        "Infra/providers.tf",
        "Infra/terraform.tfvars",
        "Infra/variables.tf",
        "k8s/app-deployment.yml",
        "__init__.py",
        "config.py",
        "creds.json",
        "main.py",
        "qdrant_engine.py",
        "readme.md",
        "requirements.txt",
    ]

    for file in files:
        file_path = os.path.join(base_folder, file)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            f.write("# This is a placeholder file.")

if __name__ == "__main__":
    create_folder_structure()
    print("Folder structure created successfully.")
