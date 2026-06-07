# Vtuber AI Assistant

[![CI](https://github.com/advent06564/Vtuber-AI-assistant/actions/workflows/ci.yml/badge.svg)](https://github.com/advent06564/Vtuber-AI-assistant/actions/workflows/ci.yml)

> *A modular, extensible framework for building an AI-powered VTuber assistant with a custom front end.*

A hybrid assistant framework that lets you pair a custom VTuber avatar front end with any AI model of your choice — cloud API, local LLM, or custom endpoint. Designed to be modular: swap models, add capabilities, and customize the personality without touching the core framework.

## 🎯 Features

- **Modular AI Backend** — Plug in any LLM (OpenAI, Anthropic, local models via Ollama/LM Studio, etc.)
- **CLI Interface** — Interactive chat mode for testing and development
- **Status Dashboard** — Check configuration and runtime state via CLI
- **VTuber-Ready** — Designed to integrate with Live2D, VRoid, or Three.js avatar front ends
- **Extensible** — Add new commands and capabilities through a clean class-based architecture

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| **Core** | Python 3.x |
| **CLI** | Standard library (`sys`, `input`) |
| **AI (pluggable)** | Your choice — OpenAI API, Anthropic, Ollama, LM Studio, etc. |
| **Frontend (future)** | Live2D / VRoid / Three.js + WebSocket bridge |

## 📁 Project Structure

```text
Vtuber-AI-assistant/
├── main.py         # Core assistant class + CLI entry point
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** installed

### Run the Assistant

```bash
# Interactive chat mode (default)
python main.py chat

# Check configuration and status
python main.py status
```

### Chat Mode Example

```
  Aurora AI Assistant - type 'exit' to quit

  You: Hello!
  Aurora: [echo] Hello!

  You: exit
  Aurora: Goodbye!
```

## 🔌 Integrating an AI Model

The `VtuberAI.chat()` method contains a placeholder echo loop. To connect a real AI model, replace the echo line with your API call:

```python
# Example: OpenAI integration
import openai

def chat(self) -> None:
    # ... existing setup ...
    elif user_input:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        print(f"  {self.name}: {response.choices[0].message.content}")
```

## 🎨 VTuber Frontend Integration (Planned)

The framework is designed to communicate with a VTuber frontend via:

1. **WebSocket Server** — Stream AI responses to a browser-based avatar
2. **Live2D SDK** — Drive expressions and lip-sync from AI output
3. **Voice Synthesis** — Add TTS for spoken responses (ElevenLabs, Azure, etc.)

## 🧩 Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  VTuber Frontend │◄───►│  WebSocket Bridge │◄───►│  VtuberAI Core  │
│  (Live2D/VRoid)  │     └──────────────────┘     │  (Python)       │
└─────────────────┘                                │  ┌───────────┐  │
                                                   │  │ AI Backend│  │
                                                   │  │ (pluggable)│  │
                                                   │  └───────────┘  │
                                                   └─────────────────┘
```

---

*Built as an extensible foundation for AI-powered VTuber experiences.*
