# AI News Crew - Agentic AI with CrewAI + Gemini

An AI-powered multi-agent pipeline that researches any topic on the web and automatically writes a polished blog post about it. Fully autonomous, end to end.

Built with **CrewAI**, **Google Gemini 2.5 Flash**, and **Serper** (Google Search API).

---

## How It Works

Two AI agents collaborate in sequence:

```
User Input (topic)
      |
      v
+---------------------+
|   Senior Researcher  |  <- Searches the web, analyzes trends,
|                      |     pros/cons, risks, opportunities
+----------+----------+
           |
           v
+---------------------+
|       Writer         |  <- Takes research output, writes an
|                      |     engaging, easy-to-read article
+----------+----------+
           |
           v
   new-blog-post.md
```

---

## Project Structure

```
agentic_ai_crew/
|-- agents.py         # Defines the Researcher and Writer agents
|-- tasks.py          # Defines what each agent is supposed to do
|-- tools.py          # Sets up the Serper web search tool
|-- crew.py           # Wires everything together and kicks off execution
|-- new-blog-post.md  # Auto-generated output article
|-- .env              # API keys (not committed to git)
|-- requirements.txt
```

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/vidush1104/researchwriter.git
cd agentic_ai_crew
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install crewai python-dotenv crewai-tools
```

### 4. Set up your .env file

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
SERPER_API_KEY=your_serper_api_key
```

Get your keys here:
- Gemini API Key -> https://aistudio.google.com
- Serper API Key -> https://serper.dev

### 5. Run the crew

```bash
python crew.py
```

The generated article will be saved to `new-blog-post.md`.

---

## Configuration

To change the research topic, edit the last line in `crew.py`:

```python
result = crew.kickoff(inputs={'topic': 'Your topic here'})
```

To swap the LLM, update `agents.py`:

```python
llm = LLM(
    model="gemini/gemini-2.5-flash",   # or gemini/gemini-2.5-pro, etc.
    temperature=0.5,
    api_key=os.getenv("GOOGLE_API_KEY")
)
```

---

## Tech Stack

| Tool | Purpose |
|---|---|
| [CrewAI](https://crewai.com) | Multi-agent orchestration framework |
| [Google Gemini 2.5 Flash](https://aistudio.google.com) | LLM powering both agents |
| [Serper](https://serper.dev) | Real-time Google Search API |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## Example Output

**Topic:** *"Will AI take jobs"*

> Forget the doomsday predictions! The conversation around AI and jobs is shifting from fear to excitement, focusing on how artificial intelligence is transforming, rather than replacing, our work...

Full output saved to `new-blog-post.md` after each run.

---

## .gitignore

Make sure your `.env` is never pushed to GitHub. Your `.gitignore` should include:

```
.env
venv/
__pycache__/
*.pyc
new-blog-post.md
```

---

## Author

Built by **Vidush** - learning agentic AI one crew at a time.
