from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime
import json
import os


def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


save_tool = Tool(
    name="save_text_to_file",
    func=save_to_txt,
    description="Saves structured research data to a text file.",
)


search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func=search.run,
    description="Search the web for information",
)


def save_code_and_readme(data):
    import json

    # data might be a string (JSON) or dict
    if isinstance(data, str):
        try:
            payload = json.loads(data)
        except json.JSONDecodeError as e:
            return f"Error decoding JSON: {e}\nData received: {data}"
    elif isinstance(data, dict):
        payload = data
    else:
        return f"Unexpected input type: {type(data)}"

    # Check required keys
    required_keys = ["filename", "language", "code", "instructions"]
    if not all(k in payload for k in required_keys):
        return f"Missing required keys: {required_keys}"

    filename = payload["filename"]
    language = payload["language"].lower()
    code = payload["code"]
    instructions = payload["instructions"]

    ext_map = {
        "python": ".py",
        "javascript": ".js",
        "typescript": ".ts",
        "php": ".php",
        "java": ".java",
        "c++": ".cpp",
        "c": ".c",
        "html": ".html",
        "css": ".css",
        "json": ".json",
        "markdown": ".md",
        "bash": ".sh"
    }

    # Ensure correct extension
    if not any(filename.endswith(ext) for ext in ext_map.values()):
        filename += ext_map.get(language, ".txt")

    # Prevent overwrite
    import os
    from datetime import datetime
    if os.path.exists(filename):
        base, ext = os.path.splitext(filename)
        filename = f"{base}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}"

    # Save code
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)

    # Save README
    readme_file = f"{os.path.splitext(filename)[0]}_README.txt"
    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(instructions)

    return f"Saved {filename} ({language}) and {readme_file}"


save_code_tool = Tool(
    name="save_code_files",
    func=save_code_and_readme,
    description="Saves code and instructions into separate files."
)


api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
