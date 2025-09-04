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
```
2. Créer et activer un environnement virtuel :
 ```bash
  python -m venv .venv
  source .venv/bin/activate   # sous Linux/Mac
  .venv\Scripts\activate      # sous Windows
```

3. Installer les dépendances :
 ```bash
pip install -r requirements.txt
pip install -U ddgs
```

## Configuration requise
- Python 3.10+
- Node.js (pour JavaScript/TypeScript code)
- PHP (pour PHP code)
- OpenJDK (pour Java code)

Installez les dépendances système séparément à l’aide du gestionnaire de packages de votre système d’exploitation :
- Ubuntu/Debian: `sudo apt install nodejs php openjdk-17-jdk`
- macOS (Homebrew): `brew install node php openjdk`


##  Configuration

Créez un fichier .env à la racine du projet avec vos clés API :
 ```bash
OPENAI_API_KEY="votre_cle_openai"
ANTHROPIC_API_KEY="votre_cle_anthropic"
```

## Utilisation

Lancez le programme :
 ```bash
python main.py
```
L’agent vous demandera une requête :
 ```bash
What can i help you research?

```
Exemple de requêtes :
- Fais-moi un résumé de l’histoire de Python et sauve dans un fichier

## Choix du modèle (OpenAI ou Anthropic)
Dans main.py, décommentez la ligne correspondant au LLM souhaité :
 ```bash
# Utiliser OpenAI
# llm = ChatOpenAI(model="gpt-4o-mini")

# Utiliser Anthropic
llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

```
