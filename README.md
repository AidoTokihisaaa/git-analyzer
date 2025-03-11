### **📌 README.md - Documentation Complète pour `git-analyzer`**
Ce fichier **README** explique **comment cloner le dépôt**, **installer l’environnement**, **configurer les dépendances** et **lancer l’API FastAPI**.

---

# **Git Analyzer**
📌 **Un projet FastAPI permettant d’analyser un repository GitHub, d’indexer son contenu et de faire des recherches sémantiques dans le code source.**  
💻 **Technologies utilisées** :  
- **FastAPI** - API REST  
- **pygit2** - Clonage et gestion de repositories Git  
- **LlamaIndex** - Indexation de fichiers  
- **Milvus** - Base de données vectorielle  
- **Docker** - Déploiement simplifié  

---

## **📌 1. Cloner le projet**
Exécute cette commande pour **cloner le dépôt sur ta machine** :
```bash
git clone https://github.com/AidoTokihisaaa/git-analyzer.git
cd git-analyzer
```

---

## **📌 2. Installer l’environnement virtuel**
💡 **Créer et activer un environnement virtuel Python**
```bash
python3 -m venv venv
source venv/bin/activate  # Sous Windows : venv\Scripts\activate
```

---

## **📌 3. Installer les dépendances**
Une fois l’environnement activé, installe toutes les bibliothèques requises :
```bash
pip install -r requirements.txt
```

---

## **📌 4. Configurer les variables d’environnement**
1️⃣ **Créer un fichier `.env` dans le projet**  
```bash
touch .env
```
2️⃣ **Ajouter les variables nécessaires :**
```
MILVUS_HOST=localhost
MILVUS_PORT=19530
REPO_BASE_PATH=src/repos
```

---

## **📌 5. Lancer Milvus (Base de données vectorielle)**
🚀 **Milvus** est utilisé pour stocker les embeddings vectoriels.  
Exécute cette commande pour le lancer dans **Docker** :
```bash
docker run -d --name milvus -p 19530:19530 milvusdb/milvus:v2.1.4
```
💡 **Vérifier que Milvus tourne bien** :
```bash
docker ps
```
Si tu ne vois pas `milvus`, démarre-le :
```bash
docker start milvus
```

---

## **📌 6. Lancer l’API FastAPI**
Démarre **FastAPI** avec la commande :
```bash
uvicorn src.main:app --reload
```
Si tu as une erreur `ModuleNotFoundError`, lance plutôt :
```bash
PYTHONPATH=src uvicorn src.main:app --reload
```
Ou sous **Windows PowerShell** :
```powershell
$env:PYTHONPATH="src"; uvicorn src.main:app --reload
```
L’API tournera sur **`http://127.0.0.1:8000`**.

---

## **📌 7. Tester l’API**
💡 **Utilise `curl` pour interagir avec l’API**

### **1️⃣ Indexer un repository GitHub**
```bash
curl -X 'POST' 'http://127.0.0.1:8000/index/the/repo/url/' \
     -H 'Content-Type: application/json' \
     -d '{"repo_url": "https://github.com/tiangolo/fastapi", "branch": "main"}'
```

### **2️⃣ Vérifier l'état d'indexation**
```bash
curl -X 'GET' 'http://127.0.0.1:8000/index/the/repo/url/?repo_url=https://github.com/tiangolo/fastapi'
```

### **3️⃣ Rechercher du code**
```bash
curl -X 'GET' 'http://127.0.0.1:8000/search/the/repo/url/?query=requests'
```

---

## **📌 8. Déployer avec Docker**
Tu peux aussi exécuter le projet directement avec **Docker**.

### **1️⃣ Construire l’image**
```bash
docker build -t git-analyzer .
```

### **2️⃣ Lancer le conteneur**
```bash
docker run -p 8000:8000 git-analyzer
```
L’API sera disponible sur **`http://127.0.0.1:8000`**.

---

## **📌 9. Problèmes courants et solutions**
| 🚨 **Problème** | ✅ **Solution** |
|----------------|--------------|
| `Permission denied (publickey)` lors de `git push` | Ajoute ta clé SSH à GitHub ou utilise HTTPS |
| `ModuleNotFoundError: No module named 'config'` | Ajoute `src/` au `PYTHONPATH` (`export PYTHONPATH=src`) |
| `OSError: Address already in use` lors de `uvicorn` | Trouve et tue le processus : `kill -9 $(lsof -t -i:8000)` |
| `Connection refused` sur Milvus | Assure-toi que Milvus tourne (`docker ps`) et redémarre-le (`docker start milvus`) |

---

## **📌 10. Contribuer**
Les contributions sont les bienvenues !  
1. **Fork le repo**
2. **Crée une branche (`git checkout -b feature-xxx`)**
3. **Fais tes modifications**
4. **Commit (`git commit -m "Ajout de xxx"`)**
5. **Push (`git push origin feature-xxx`)**
6. **Ouvre une pull request sur GitHub**

---

## **📌 11. Auteur**
👤 **AidoTokihisaaa**  
📌 **GitHub** : [AidoTokihisaaa](https://github.com/AidoTokihisaaa)
