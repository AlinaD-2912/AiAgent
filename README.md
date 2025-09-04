# AiAgent

AiAgent est un projet Python qui permet de créer un agent IA local basé sur LangChain, avec la possibilité d’utiliser au choix OpenAI ou Anthropic Claude comme LLM (modèle de langage).
L’agent peut effectuer des recherches sur Internet ou générer du code dans plusieurs langages, et sauvegarder les résultats ou fichiers de code sur demande.


##  Fonctionnalités
1. Choix du LLM :

    - OpenAI GPT (ChatOpenAI)
    - Anthropic Claude (ChatAnthropic)
    (il suffit de commenter/décommenter une ligne dans le code)

2. Modes de fonctionnement

  - Mode recherche

    - Effectue des recherches via Wikipédia ou un moteur de recherche (DuckDuckGo).

    - Résume les informations et peut sauvegarder les résultats dans un fichier .txt.

  - Mode codage

    - Génère du code dans plusieurs langages : Python, JavaScript, TypeScript, PHP, Java, HTML/CSS, Bash, etc.

  - Fournit toujours :

    - filename (nom du fichier avec extension correcte)

    - language (langage de programmation)

    - code (le code source complet)

    - instructions (README expliquant les dépendances, l’usage, etc.)

  - Sauvegarde automatiquement le code et un fichier README associé.
  - 
3. Outils intégrés

  - Recherche générale (DuckDuckGo)

  - Recherche Wikipédia

  - Sauvegarde des résultats dans un fichier .txt

  - Sauvegarde de code et instructions dans des fichiers séparés (.py, .js, .php, .java, _README.txt, etc.)


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
Exemple d’utilisation
Mode recherche
```bash
Choose mode (research/coding): research
What can I help you research?
```
Exemple de requête :

“Fais-moi un résumé de l’histoire de Python et sauve dans un fichier”

Mode codage
```bash
Choose mode (research/coding): coding
What can I help you code? 

```

Exemple de requête :

“Crée un script Python pour afficher ‘Hello World’ et explique comment l’exécuter.”

## Choix du modèle (OpenAI ou Anthropic)
Dans main.py, décommentez la ligne correspondant au LLM souhaité :
 ```bash
# Utiliser OpenAI
# llm = ChatOpenAI(model="gpt-4o-mini")

# Utiliser Anthropic
llm = ChatAnthropic(model="claude-3-5-sonnet-20240620")

```
