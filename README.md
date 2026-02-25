# Atlas User & Product Management API

## 📌 Project Overview

This project is a **FastAPI backend application** connected to **MongoDB Atlas** that manages **Users** and **Products**.

It demonstrates:

* REST API development using FastAPI
* Cloud database integration using MongoDB Atlas
* Request validation using Pydantic
* Error handling using HTTPException
* Docker containerization
* API testing via Swagger UI and Postman

---

## 🧱 Project Structure

```
atlas_user_product_api/
│
├── app/
│   ├── main.py        # API endpoints
│   ├── database.py    # MongoDB connection
│   ├── schemas.py     # Pydantic models
│
├── requirements.txt
├── Dockerfile
├── .env
```

---

## ⚙️ Technologies Used

* FastAPI
* MongoDB Atlas
* PyMongo
* Pydantic
* Uvicorn
* Docker

---

## 🗄️ Database

MongoDB Atlas cloud database is used.

Collections created:

* users
* products

---

## 🚀 API Endpoints

### 👤 User APIs

#### Create User

POST `/users`

Creates a new user after validating request data and checking duplicate email.

#### Get User by Email

GET `/users/{email}`

Fetches user details from database.

---

### 📦 Product APIs

#### Create Product

POST `/products`

Creates a product after checking duplicate SKU.

#### Get Product by SKU

GET `/products/{sku}`

Fetches product details.

---

## ✅ Validation & Error Handling

* Pydantic models ensure request validation
* Duplicate checks using `find_one()`
* HTTPException used for proper error responses

---

## ▶️ How to Run Project

### Install dependencies

```
pip install -r requirements.txt
```

### Start server

```
uvicorn app.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Docker Setup

### Build image

```
docker build -t atlas-api .
```

### Run container

```
docker run -p 8000:8000 atlas-api
```

---

## 🧪 Testing

APIs tested using:

* Swagger UI
* Postman

---

## 🎯 Learning Outcomes

* FastAPI backend development
* NoSQL database integration
* Request vs Response schema understanding
* Docker containerization workflow
* REST API design principles

---

## 👩‍💻 Author

Student Project – Atlas User & Product API
