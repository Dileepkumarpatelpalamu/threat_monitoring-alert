# Threat Monitoring & Alert Management Backend

## 📌 Project Overview

This project is a **Backend API System for a simplified Threat Monitoring & Alert Management Platform**, built using **Django** and **Django REST Framework (DRF)**.

The system ingests security events, automatically generates alerts for **High/Critical severity events**, and provides secure, role-based access to alert data. It follows **REST best practices** with proper HTTP status codes, pagination, and input validation.

---

## 🛠 Tech Stack

* **Backend:** Python, Django
* **API Framework:** Django REST Framework (DRF)
* **Authentication:** JWT (SimpleJWT)
* **Database:** PostgreSQL / SQLite
* **Version Control:** Git

### Optional Enhancements

* Swagger / Postman API documentation
* Docker setup
* Unit tests
* Deployment steps (AWS / EC2 / Render / Railway)

---

## 🔐 Authentication & Authorization

JWT-based authentication implemented using **djangorestframework-simplejwt**.

### Roles

* **Admin:** Full access (manage events & alerts)
* **Analyst:** Read-only access to alerts

---

## 📂 API Endpoints

### 🔑 Authentication

| Method | Endpoint              | Description                       |
| ------ | --------------------- | --------------------------------- |
| POST   | `/api/token/`         | Obtain JWT access & refresh token |
| POST   | `/api/token/refresh/` | Refresh JWT access token          |

---

### 📥 Events API

| Method      | Endpoint            | Description               | Access |
| ----------- | ------------------- | ------------------------- | ------ |
| GET         | `/api/events/`      | List all security events  | Admin  |
| POST        | `/api/events/`      | Ingest new security event | Admin  |
| GET         | `/api/events/{id}/` | Retrieve event details    | Admin  |
| PUT / PATCH | `/api/events/{id}/` | Update event              | Admin  |
| DELETE      | `/api/events/{id}/` | Delete event              | Admin  |

---

### 🚨 Alerts API

| Method | Endpoint            | Description            | Access          |
| ------ | ------------------- | ---------------------- | --------------- |
| GET    | `/api/alerts/`      | List alerts            | Admin / Analyst |
| GET    | `/api/alerts/{id}/` | Retrieve alert details | Admin / Analyst |
| PATCH  | `/api/alerts/{id}/` | Update alert status    | Admin only      |

**Filtering supported:**

```http
GET /api/alerts/?severity=High&status=Open
```

---

## 🗄 Data Models

### Event

* source (string)
* event_type (intrusion, malware, anomaly)
* severity (Low / Medium / High / Critical)
* description
* timestamp (auto-generated)

### Alert

* event (ForeignKey → Event)
* status (Open / Acknowledged / Resolved)
* created_at

---

## 🔒 Security Practices

* Secure JWT token handling
* Role-based permission checks
* Input validation & error handling
* Prevention of SQL injection & misuse
* Avoid sensitive data exposure
* Clean separation of concerns (models, serializers, views)

---

## ⚙️ Setup Instructions

```bash
git clone <repository-url>
cd project-name
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate   # Windows
pip install -r requirements.txt
# OR if requirements.txt not available:
pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 📦 Deliverables

* GitHub repository link
* Complete Django project
* README.md (overview, setup, endpoints, assumptions)
* Optional: Postman collection, architecture diagram, `.env.example`

---

## 📌 Assumptions

* Alerts are generated only for **High** and **Critical** severity events
* Analysts have read-only access to alerts
* Admin users manage the complete alert lifecycle

---

## 👨‍💻 Author

**Dileep Kumar Patel**

---

## 📅 Submission

Django Developer Assignment – **Cyethack Solutions Private Limited**
