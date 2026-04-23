# 🚀 Web Intelligence Aggregator

A production-style data aggregation system that extracts and analyzes structured data from multiple domains such as e-commerce and news.

---

## 🔧 Features
- Multi-domain scraping (E-commerce, News)
- Data extraction using BeautifulSoup
- Aggregation (sum, views, analytics)
- REST API using FastAPI
- Containerized using Docker
- Deployable on Google Cloud Run

---

## 📌 Endpoints

### GET /
Check service status

### GET /ecommerce/total
Returns total inventory value

### GET /news/views
Returns total article views

---

## 🧠 Architecture
- Scraper layer → Extracts structured data
- API layer → Exposes results via endpoints
- Docker → Containerized deployment
- Cloud Run → Scalable hosting

---

## 🚀 Run Locally

```bash
pip install -r requirements.txt
uvicorn api.main:app --reload

## Docker Run
docker build -t aggregator .
docker run -p 8080:8080 aggregator

## Deploy GCP
gcloud builds submit --tag gcr.io/$PROJECT_ID/aggregator
gcloud run deploy aggregator --image gcr.io/$PROJECT_ID/aggregator --allow-unauthenticated
