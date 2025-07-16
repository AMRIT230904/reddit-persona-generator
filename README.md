# Reddit User Persona Generator 🧠

This tool takes a Reddit username and generates a detailed user persona based on their public posts and comments using an LLM.
This tool analyzes a Reddit user’s public activity and generates a detailed user persona using their posts and comments.  
It uses Large Language Models (LLMs) to derive personality traits, interests, writing style, and behavioral patterns.

---

## 📦 Tech Stack
- Python
- PRAW (Reddit API wrapper)
- OpenAI API (GPT-3.5)
- `.env` for secure credential management

---

## 🚀 How to Run

1. **Clone the repository**
```bash
git clone https://github.com/your-username/reddit-persona-gen.git
cd reddit-persona-gen



⚠️ **Note: OpenAI API Quota**

Due to limited free-tier API credits, the current OpenAI API key in the `.env` file may not work or may be exhausted.  
To run the project successfully, please:

1. Create your own API key at https://platform.openai.com/account/api-keys
2. Add it to your `.env` file like this:

