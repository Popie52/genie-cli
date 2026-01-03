# Genie CLI

**Genie CLI** is a local interactive AI assistant powered by Google Gemini API.  
It can read and analyze your local code files, run Python scripts, and assist with debugging — all through a simple command-line interface.  

---

## Features

- Interactive chat assistant for your projects.
- Reads and analyzes local Python files.
- Executes Python scripts and returns results.
- Persistent local chat history.
- Handles Gemini API quota limits gracefully.
- Supports function calls for automation tasks in your code.

---

## Requirements

- Python 3.10+
- [UltraViolet (uv)](https://pypi.org/project/uv/) CLI runner
- Google Gemini API key

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Popie52/genie-cli.git
cd genie-cli
```
2. Create a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install uv
```

4. Create a .env file in the root of the project and add your Gemini API key:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```
## Usage

Start the interactive assistant:
```bash
uv run main.py
```

You will see:
```bash
Chat assistant ready! Type 'exit' to quit.
You:
```


* Type your question or command.

* The assistant will read local files, analyze code, or execute scripts as needed.

* To exit, type:
```bash
exit
```


or
```bash
quit
```

## Notes

* Chat history is saved locally in ```chat_history.json```. You can continue your conversation even after restarting.

* If the Gemini API quota is exceeded, the assistant will inform you and ```resume after 24 hours```.

* Make sure your ```.env``` file is never pushed publicly.

## Contributing

Contributions are welcome!
Feel free to open issues, submit pull requests, or suggest new features.