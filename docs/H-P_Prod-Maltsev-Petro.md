# Cahier des Charges : Stand de Migration de Données F1

## 1. Objectifs du Projet
* **Conteneurisation :** Concevoir un environnement réseau et serveur entièrement conteneurisé.
* **Automatisation :** Développer un script d'automatisation ETL (*Extract, Transform, Load*) simple en Python.
* **Migration :** Assurer le transfert structuré d'un jeu de données relationnel existant vers un nouveau SGBD.

## 2. Spécifications Techniques

| Composant | Technologie Requise | Rôle dans le projet |
| :--- | :--- | :--- |
| **Source de données** | MySQL 5.7.11 | Hébergement des données brutes via l'importation automatique d'un dump SQL au démarrage. |
| **Cible de données** | PostgreSQL 18 | Base de destination avec un schéma optimisé (clés primaires, contraintes d'intégrité). |
| **Logique de migration** | Python 3.11+ | Script exécutant l'extraction et l'insertion via `psycopg` et `mysql-connector-python`. |
| **Orchestration** | Docker & Docker Compose | Gestion du réseau interne, des volumes persistants et de l'ordre de démarrage. |

## 3. Livrables Attendus
* **`docker-compose.yml` :** Fichier fonctionnel déployant les trois services de manière autonome.
* **`Dockerfile` :** Configuration de l'environnement d'exécution pour le script Python.
* **`migrate.py` :** Script documenté avec des commentaires clairs, capable de migrer au moins 4 tables distinctes (*pilotes, circuits, courses, résultats*).
* **`README.md` :** Guide court expliquant les commandes nécessaires pour lancer le stand (`docker compose up -d`).

## 4. Contraintes de Réalisation
* **Indépendance :** Le code doit rester suffisamment basique pour être compris, débogué et soutenu devant un formateur sans l'aide d'une IA.
* **Sécurité réseau :** Les conteneurs doivent communiquer via le réseau interne de Docker (résolution DNS par nom de service/conteneur).
* **Gestion des erreurs :** Le script Python doit inclure des blocs `try/except` rudimentaires pour éviter un crash si MySQL met trop de temps à démarrer.
* **Optimisation des données :** Le schéma de la base PostgreSQL cible ne doit pas être une copie aveugle ; il faut corriger les types de données (par exemple, forcer un `VARCHAR(3)` pour les codes de pilotes au lieu d'un `TEXT` générique).