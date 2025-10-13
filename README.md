# 🧠 AI Customer Support Agent (RAG + LLM + Redis + Ticketing + Monitoring)

![AI Support Agent Flow](flowchart.png)

Welcome to the **AI Customer Support Agent**, a production-ready backend system that demonstrates advanced AI workflows with **Retrieval-Augmented Generation (RAG)**, LLM reasoning, caching, ticketing, and monitoring.

---

## ✨ Features

- **Semantic Search**: Retrieve relevant context from PDFs, FAQs, and knowledge base using **ChromaDB / FAISS**
- **LLM Agent**: Generate intelligent responses using **Ollama or OpenAI**
- **Redis Memory & Cache**: Speed up responses and maintain per-user context
- **Ticketing System**: Auto-create tickets for unanswered or low-confidence queries
- **Analytics Dashboard**: Track queries, cache hits, tickets, and visualize metrics
- **Monitoring**: **Prometheus + Grafana** integration for real-time metrics
- **Dockerized**: Easy setup and deployment across environments

---

## 🚀 Quick Setup

### 1️⃣ Clone Repository
```bash
git clone [https://github.com/vickytilotia/AI_Support_Agent.git](https://github.com/vickytilotia/AI_Support_Agent.git)
cd AI-Support-Agent
```

### 2️⃣ Python Environment
```bash
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

### 3️⃣ Docker Setup
```bash
docker-compose up --build
```
Access services:
- FastAPI → [http://localhost:8000](http://localhost:8000)
- Prometheus → [http://localhost:9090](http://localhost:9090)
- Grafana → [http://localhost:3000](http://localhost:3000) (admin/admin)

### 4️⃣ Initialize Database
Tables auto-create on FastAPI startup.
```bash
uvicorn app.main:app --reload
```

### 5️⃣ Test Endpoints
- **Chat**: POST `/chat/` → Send user query
- **Analytics**: GET `/analytics/` → View system metrics

---

## 📊 Project Flow

```text
User Query
   │
   ▼
ChromaDB / FAISS (RAG) → Retrieve context
   │
   ▼
LLM Agent → Generate Answer
   │
   ├─> Redis Cache → Check / Store
   └─> If Low Confidence → Create Ticket (SQLite)
   │
   ▼
Update Analytics → Prometheus Scrapes → Grafana Visualizes
```
*Flowchart image: `flowchart.png`*

---

## 🖼️ Screenshots (Placeholders)

| Scenario | Screenshot |
|----------|------------|
| Query & Answer | ![Query & Answer](screenshots/query_answer.png) |
| Query & Answer from Cache | ![Cache Hit](screenshots/cache_hit.png) |
| Ticket Creation | ![Ticket Created](screenshots/ticket_created.png) |

*(Replace placeholders with actual images to make it visually interactive.)*

---

## 📁 Folder Structure
```
AI-Support-Agent/
├─ app/
│  ├─ api/            # FastAPI routes
│  ├─ services/       # LLM, RAG, Memory, Ticket, Analytics
│  ├─ core/           # DB and Redis setup
│  ├─ main.py         # FastAPI entrypoint
├─ data/              # SQLite DB
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ prometheus.yml
├─ flowchart.png      # Visual project flow
├─ README.md          # Project documentation
```

---

## 🌟 Next Steps / Enhancements
- Add **API authentication** (API keys / OAuth2)
- Implement **Celery async tasks** for ticket notifications
- Build **frontend dashboard** for queries and analytics
- Enhance **Grafana dashboards** with user-level metrics
- Demonstrate **multi-instance scaling** with Docker Compose

---

## 📝 License
MIT License