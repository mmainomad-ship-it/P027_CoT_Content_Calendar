# P027: Chain-of-Thought Content Calendar Generator 📅

## 📝 Description
This project demonstrates **Prompt Chaining** and **Chain-of-Thought (CoT)** reasoning using a Local LLM. Instead of a single generic prompt, the script breaks the task into three distinct stages: Idea Generation, Strategic Filtration, and Schedule Structuring. The output of one step serves as the input for the next.

## 🚀 Key Features
* **Chain-of-Thought Prompting:** Forces the model to reason about target audiences before generating ideas.
* **Prompt Chaining:** Uses the output of the brainstorming phase as context for the selection phase.
* **Structured Output:** Generates a clean Markdown table for the final weekly schedule.
* **Local AI Power:** Runs entirely locally using Ollama.

## 🛠️ Technology Stack
* **Language:** Python 3.x
* **AI Engine:** Ollama (Local LLM)
* **Technique:** Sequential Prompt Chaining

## ⚙️ Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Ensure Ollama is running (`ollama serve`).
4. Run the script: `python calendar_agent.py`

## 👨‍💻 Author
**mmainomad-ship-it**
[GitHub Profile](https://github.com/mmainomad-ship-it)