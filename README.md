# 🎙️ Voice AI Agent

### Local AI System for Voice-Based Automation

---

## 🚀 Overview

The **Voice AI Agent** is an end-to-end intelligent system that converts human speech into actionable tasks using modern AI components.

It integrates:

* **Speech Recognition (STT)**
* **Large Language Models (LLMs)**
* **Intent Classification**
* **Automated Tool Execution**
* **Interactive UI**

This project demonstrates how multiple AI systems can be orchestrated to build a **real-world autonomous agent**.

---

## 🧠 Problem Statement

Most AI systems today are limited to text-based interactions. This project solves that limitation by enabling:

> 🎯 **Voice-driven automation on a local machine**

Users can simply speak commands like:

* “Create a file”
* “Write a Python function”
* “Summarize this text”

…and the system executes them automatically.

---

## 🏗️ System Architecture

```text
Audio Input
   ↓
Speech-to-Text (Whisper)
   ↓
Text Output
   ↓
Intent Classification (LLM via Ollama)
   ↓
Action Mapping
   ↓
Tool Execution (File Ops / Code / Summary)
   ↓
Result Display (Streamlit UI)
```

---

## ⚙️ Tech Stack

### 🔊 Speech Processing

* **OpenAI Whisper**

  * Converts audio → text
  * High accuracy speech recognition

### 🤖 Language Model

* **Ollama (Mistral)**

  * Runs locally
  * Handles intent classification
  * Eliminates dependency on external APIs

### 🧩 Backend Logic

* **Python**

  * Modular architecture
  * Handles pipeline orchestration

### 🛠️ Tools Layer

* File system automation
* Code generation
* Text summarization

### 🌐 Frontend

* **Streamlit**

  * Lightweight UI
  * Real-time interaction

### 🎧 Audio Processing

* **FFmpeg**

  * Required for Whisper audio decoding

---

## 📂 Project Structure

```text
voice_ai_agent/
│
├── app.py                  # Main UI & pipeline integration
├── requirements.txt
├── README.md
│
├── stt/                    # Speech-to-Text module
│   └── speech_to_text.py
│
├── llm/                    # LLM intent classifier
│   └── intent_classifier.py
│
├── tools/                  # Action execution layer
│   ├── file_ops.py
│   ├── code_generator.py
│   └── summarizer.py
│
├── utils/                  # Helper utilities
│
└── output/                 # Generated files (safe directory)
```

---

## 🔥 Features

✅ Voice input via audio file
✅ Accurate speech-to-text conversion
✅ Intelligent intent detection using LLM
✅ Automated file creation
✅ Dynamic code generation
✅ Text summarization
✅ Clean and interactive UI
✅ Fully local execution (no cloud dependency)

---

## 🧪 Example Use Cases

### 🎤 Input:

> “Create a file”

### ⚙️ Output:

* File created in `output/new_file.txt`

---

### 🎤 Input:

> “Write a Python function to add two numbers”

### ⚙️ Output:

* Code generated and saved automatically

---

### 🎤 Input:

> “Summarize this text…”

### ⚙️ Output:

* Concise summary generated using LLM

---

## 🛡️ Safety Design

To prevent unintended system modifications:

> 📁 All file operations are restricted to the `output/` directory

---

## 🧑‍💻 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/voice-ai-agent.git
cd voice-ai-agent
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Install FFmpeg

* Download and add to system PATH

---

### 5️⃣ Run Ollama (Local LLM)

```bash
ollama run mistral
```

---

### 6️⃣ Launch Application

```bash
python -m streamlit run app.py
```

---

## 📸 Demo Flow

1. Upload audio file
2. System transcribes speech
3. LLM detects intent
4. Action is executed
5. Output is displayed

---

## ⚡ Key Highlights

* 🔥 Fully **local AI pipeline**
* 🧠 Combines **multiple AI domains**
* 🏗️ Clean **modular architecture**
* ⚙️ Real-world **automation capability**
* 📈 Strong **portfolio-level project**

---

## 🚧 Challenges Faced

* Managing local model execution (Ollama)
* Handling audio processing dependencies (FFmpeg)
* Ensuring correct intent classification
* Resolving environment and dependency conflicts

---

## 🚀 Future Improvements

* 🎯 Multi-intent command handling
* 💬 Full conversational chat system
* 🧠 Memory & context awareness
* 🔁 Real-time microphone input
* 📊 Model benchmarking

---

## 📚 Learnings

* End-to-end AI system design
* Integration of STT + LLM + automation
* Handling real-world system dependencies
* Building modular and scalable pipelines

---

## 🙌 Conclusion

This project demonstrates how modern AI components can be combined to build a **fully functional voice-driven automation system**.

It bridges the gap between:

> 🧠 Intelligence (LLMs) and ⚙️ Action (System Execution)

---

## 👨‍💻 Author

**Jayanth M**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it helps!
