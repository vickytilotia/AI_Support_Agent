# 🧠 AI Customer Support Agent (RAG + LLM + Redis + Ticketing + Monitoring)


Welcome to the **AI Customer Support Agent**, a production-ready backend system that demonstrates advanced AI workflows with **Retrieval-Augmented Generation (RAG)**, LLM reasoning, caching, ticketing, and monitoring. Its a customer support system that automatically answers user queries, tracks unanswered questions via a ticketing system, and provides real-time analytics through a dashboard. Demonstrates caching, context-aware responses, and monitoring to ensure reliable performance and actionable insights.

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
| Query & Answer | <img width="1476" height="671" alt="query answer" src="https://github.com/user-attachments/assets/375eb78f-fb1c-423b-ad2a-0e6cbe013539" /> |
| Query & Answer from Cache | <img width="1480" height="622" alt="query answer from cache" src="https://github.com/user-attachments/assets/e8c18027-ee6a-4873-af51-1b4c7e4e6cb6" />  |
| Ticket Creation | <img width="1479" height="692" alt="creating ticket " src="https://github.com/user-attachments/assets/990ae23f-8c0a-47f7-a148-84dd9514e60e" />  |


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
