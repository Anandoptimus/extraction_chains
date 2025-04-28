# 📄 LangChain Person Information Extraction

This project uses **LangChain** and **OpenAI Function Calling** to automatically **extract person information** from a given text, such as:

- Name
- Age (if available)

It demonstrates structured extraction using **Pydantic models**, **LangChain**, and **OpenAI models**.

---

## ✨ Features

- Extracts **name** and **age** of individuals from free text.
- **Partial extraction supported**: If age is missing, only the name is extracted.
- **No hallucination**: If information is not provided explicitly, it is not guessed.
- **Built with**:
  - LangChain
  - OpenAI GPT-3.5 Turbo
  - Pydantic

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/langchain-person-extraction.git
cd langchain-person-extraction
```

### 2. Install Required Packages
- pip install -r requirements.txt

### 3. Set Your OpenAI API Key
- export OPENAI_API_KEY="your-api-key-here"

### 4. Run the Script
- python extract_person_info.py

## 📚 Notes
- No Assumptions: The model only extracts data that is explicitly mentioned.
- Partial Extraction: If only a name is mentioned without an age, it still extracts the name.

## 🤝 Contribution
- Feel free to raise Issues or Pull Requests if you want to improve the data extraction, extend fields (e.g., location, profession), or optimize the prompt.
