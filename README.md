# AiAgent

AiAgent est un projet Python qui permet de créer un agent IA local basé sur LangChain, avec la possibilité d’utiliser au choix OpenAI ou Anthropic Claude comme LLM (modèle de langage).
L’agent peut effectuer des recherches sur Internet (via Wikipédia ou un moteur de recherche) et sauvegarder les résultats dans un fichier texte sur demande.



##  Fonctionnalités
- Choix du LLM :

  - OpenAI GPT (ChatOpenAI)
  - Anthropic Claude (ChatAnthropic)
    (il suffit de commenter/décommenter une ligne dans le code)

- Exécution locale d’un agent de recherche.

- Utilisation d’outils intégrés :

  - Recherche générale

  - Recherche Wikipédia

  - Sauvegarde des résultats dans un fichier .txt

- Sauvegarde automatique possible : si votre requête contient par exemple "sauve dans un fichier", l’agent écrit le résumé dans un fichier texte.



##  Structure du projet
```bash
AiAgent/
│── main.py         # Point d’entrée du programme
│── tools.py        # Définition des outils (recherche, wiki, sauvegarde)
│── .env            # Fichier contenant vos clés API (non versionné)
│── requirements.txt # Dépendances Python
```



##  Installation

1. Cloner le dépôt :
 ```bash
  git clone https://github.com/ton-projet/AiAgent.git
  cd AiAgent
