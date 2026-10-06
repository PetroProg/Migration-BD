# Journal de travail - Projet P_Prod

**Intitulé du projet :** Migration de la base des données F1 (MySQL vers PostgreSQL)
**Établissement :** ETML (Ecole Technique des Métiers de Lausanne)   
**Auteur :** Maltsev Petro  

---

## Suivi des heures et avancement

| Date | Durée (minutes) | Tâches réalisées / Activités | Remarques, difficultés rencontrées & solutions |
| :--- | :---: | :--- | :--- |
| 01.09.2026 | 25 min | Création du projet : le cahier des charges, le journal de travail et la documentation |  |
| 01.09.2026 | 45 min | La création des scripts pour Docker (docker-compose et dockerfile) | [Documentation officielle](https://docs.docker.com/guides/pgadmin/) |
| 01.09.2026 | 45 min | Les images pour python et php apache pour les conteneurs | [Documentation sur Dockerfile](https://medium.com/@franco313mwas/building-a-scalable-etl-pipeline-from-mysql-to-postgresql-with-python-docker-airflow-4200149a0757)|
| 01.09.2026 | 20 min | Création du repo sur GitHub et premier push | [Github:repo privé](https://github.com/PetroProg) |
| 08.09.2026 | 45 min | Installation des tous les systemes et services dont Docker a besoin | [Docker images](https://hub.docker.com/) |
| 08.09.2026 | 90 min | La construction des conteneurs | Conteneurs db_sql et phpmyadmin fonctionnent |
| 22.09.2026 | 45 min | Configuration du conteneur postgresql |  |
| 22.09.2026 | 90 min | Conteneur pour le script python; Dockerfile, docker-compose.yaml |  |
| 29.09.2026 | 45 min | Ajout de .dockerignore; config de .env et dockerfile |  |
| 29.09.2026 | 90 min | Développement du script sur Python pour la migration des données. Découvrir la méthode cursor et sa fonctionnement. |  |
| 06.10.2026 | 45 min | La méthode de cursor; Le traitement des types des tables et des colonnes. |  |
| 06.10.2026 | 90 min | Obtenir les colonnes et leurs types via le script. Aussi création des conditions pour les types différents et la librarie. |  |

**Temps total cumulé :** 675 min (11 h 15 min)

