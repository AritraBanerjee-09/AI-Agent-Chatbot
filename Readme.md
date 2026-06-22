# 🤖 Personal Agentic AI Chatbot

A production-ready Agentic AI Chatbot built using LangGraph, FastAPI, Streamlit, OpenAI, Groq, and Tavily Search.

This project demonstrates how modern AI Agents can reason, use external tools, search the web, and generate context-aware responses through a scalable full-stack architecture.

---

# 🚀 Project Overview

Traditional chatbots rely solely on pre-trained knowledge and often struggle to answer:

- Recent events
- Dynamic information
- Real-time queries
- Internet-based questions

To solve this limitation, this project implements an Agentic AI architecture using LangGraph ReAct Agents.

The chatbot can:

✅ Answer general questions

✅ Use external tools

✅ Search the web when required

✅ Switch between multiple LLM providers

✅ Maintain conversation history

✅ Operate through a production-style API architecture

---

# 🎯 Problem Statement

Modern LLMs have two major limitations:

### 1. Knowledge Cutoff

LLMs only know information available during training.

Example:

"What happened in the stock market today?"

The model may not know the answer.

---

### 2. No Access To External Data

Traditional chatbots cannot:

- Search Google
- Access current news
- Fetch latest information
- Use tools dynamically

This makes them unsuitable for many real-world applications.

---

# 💡 Proposed Solution

To overcome these limitations, an Agentic AI system was developed using:

- LangGraph ReAct Agent
- Tavily Search Tool
- OpenAI Models
- Groq Models
- FastAPI Backend
- Streamlit Frontend

The agent dynamically decides:

1. Whether it can answer directly
2. Whether a search tool is required
3. How to combine retrieved information
4. How to generate the final response

---

# 🏗️ System Architecture

<p align="center">
  <img src="https://raw.githubusercontent.com/AritraBanerjee-09/AI-Agent-Chatbot/main/assets/architecture.png" width="900">
</p>
---

# ⚙️ Technical Architecture

## Frontend Layer

Technology:
- Streamlit

Responsibilities:
- User Interface
- Model Selection
- Query Input
- Chat History
- Agent Configuration

Features:
- Multi-model support
- Query history tracking
- Search toggle option
- Dynamic response rendering

---

## Backend Layer

Technology:
- FastAPI
- Pydantic

Responsibilities:
- API endpoint creation
- Request validation
- Model verification
- Agent invocation

Endpoint:

POST /chat

Input:

{
    "model_name": "llama-3.3-70b-versatile",
    "model_provider": "Groq",
    "system_prompt": "...",
    "messages": ["query"],
    "allow_search": true
}

Output:

{
    "response": "Agent Response"
}

---

## Agent Layer

Technology:
- LangGraph
- LangChain

Responsibilities:
- Reasoning
- Tool Selection
- Response Generation

Agent Type:

ReAct Agent

Reasoning Process:

Thought → Action → Observation → Final Answer

---

## Search Layer

Technology:
- Tavily Search API

Responsibilities:
- Real-time web retrieval
- Information grounding
- Current event awareness

Activated only when:

allow_search = True

---

# 🛠️ Technologies Used

| Category | Technology |
|-----------|------------|
| Programming Language | Python |
| Agent Framework | LangGraph |
| LLM Framework | LangChain |
| Backend | FastAPI |
| Frontend | Streamlit |
| Search Tool | Tavily |
| LLM Provider | OpenAI |
| LLM Provider | Groq |
| Hosting | Uvicorn |
| Validation | Pydantic |
| IDE | VS Code |

---

# ✨ Key Features

## Multi-LLM Support

Supported Models:

- GPT-4o Mini
- Llama 3.3 70B
- Mixtral 8x7B

Users can switch models dynamically.

---

## Web Search Integration

When enabled:

- Agent uses Tavily Search
- Retrieves latest information
- Produces grounded responses

---

## Agentic Reasoning

Uses LangGraph ReAct architecture.

The agent:

- Thinks
- Selects tools
- Executes actions
- Produces responses

instead of directly generating text.

---

## Conversation History

Users can:

- View previous queries
- Reload conversations
- Clear chat history

---

## Custom Agent Personality

Users can define:

- Tutor
- Interviewer
- Data Scientist
- Coding Assistant
- Research Assistant

through system prompts.

---

# 📂 Project Structure

project/
│
├── frontend.py
├── backend.py
├── ai_agent.py
├── requirements.txt
├── .env
└── README.md

---

# 🔍 Code Analysis

## ai_agent.py

Purpose:

Core AI engine.

Responsibilities:

- Load API Keys
- Initialize LLMs
- Configure Tavily Search
- Create LangGraph Agent
- Execute reasoning workflow

Key Function:

get_response_from_ai_agent()

Output:

Final AI-generated response.

---

## backend.py

Purpose:

API communication layer.

Responsibilities:

- Request validation
- Agent invocation
- Error handling
- Response generation

Framework:

FastAPI

Endpoint:

/chat

---

## frontend.py

Purpose:

User Interface

Responsibilities:

- User interaction
- Query submission
- Model selection
- Display responses
- Store session history

Framework:

Streamlit

---

# 📊 Project Analysis

## Complexity

Level:

Intermediate → Advanced

Reason:

Combines:

- Frontend Development
- Backend APIs
- Agentic AI
- LLM Integration
- Tool Calling

---

## Scalability

Current:

Single Agent Architecture

Can be extended to:

- Multi-Agent Systems
- RAG Pipelines
- Document Search
- Autonomous Agents

---

## Performance

Advantages:

✔ Fast inference using Groq

✔ Lightweight FastAPI backend

✔ Minimal latency

✔ Dynamic tool usage

---

## Security Considerations

Implemented:

- Request validation
- Allowed model restrictions

Recommended Future Improvements:

- JWT Authentication
- Rate Limiting
- API Key Encryption
- Logging & Monitoring

---

# 📈 Results

Successfully achieved:

✅ Agentic AI workflow

✅ Multi-model support

✅ Real-time web search

✅ Full-stack deployment architecture

✅ Dynamic tool calling

✅ Production-ready API integration

---

# 🚧 Challenges Faced

### API Integration

Managing multiple LLM providers with a unified interface.

### Agent Configuration

Building dynamic agents based on user-selected settings.

### Frontend-Backend Communication

Handling asynchronous API requests and responses.

### Tool Integration

Allowing the agent to decide when to use web search.

---

# 📚 Learning Outcomes

Through this project I learned:

- Agentic AI Systems
- LangGraph ReAct Agents
- Tool Calling
- FastAPI Development
- Streamlit UI Development
- API Design
- Prompt Engineering
- Multi-LLM Integration
- Production Architecture Patterns

---

# 🔮 Future Enhancements

- Memory-enabled Agents
- RAG with PDF Chat
- Vector Databases
- Multi-Agent Collaboration
- Voice Assistant Integration
- Authentication System
- Docker Deployment
- Cloud Deployment (AWS/Azure)

---

# Project Setup Guide

This guide provides step-by-step instructions to set up your project environment, including setting up a Python virtual environment using Pipenv, pip, or conda.

## Table of Contents

1. [Setting Up a Python Virtual Environment](#setting-up-a-python-virtual-environment)
   - [Using Pipenv](#using-pipenv)
   - [Using pip and venv](#using-pip-and-venv)
   - [Using Conda](#using-conda)
2. [Running the application](#project-phases-and-python-commands)


## Setting Up a Python Virtual Environment

### Using Pipenv
1. **Install Pipenv (if not already installed):**  
```
pip install pipenv
```

2. **Install Dependencies with Pipenv:** 

```
pipenv install
```

3. **Activate the Virtual Environment:** 

```
pipenv shell
```

---

### Using `pip` and `venv`
#### Create a Virtual Environment:
```
python -m venv venv
```

#### Activate the Virtual Environment:
**macOS/Linux:**
```
source venv/bin/activate
```

**Windows:**
```
venv\Scripts\activate
```

#### Install Dependencies:
```
pip install -r requirements.txt
```

---

### Using Conda
#### Create a Conda Environment:
```
conda create --name myenv python=3.11
```

#### Activate the Conda Environment:
```
conda activate myenv
```

#### Install Dependencies:
```
pip install -r requirements.txt
```


# Project Phases and Python Commands

## Phase 1: Create AI Agent
```
python ai_agent.py
```

## Phase 2: Setup Backend with FastAPI
```
python backend.py
```

## Phase 3: Setup Frontend with Streamlit
```
streamlit run frontend.py
```

# 👨‍💻 Author

Aritra Banerjee

B.Tech Electronics & Computer Science Engineering

KIIT University

Interested in:
- AI Engineering
- Machine Learning
- Data Analytics
- Generative AI



