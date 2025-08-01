# HROne-Backend-Task

### FastAPI MongoDB Backend – Product & Order API

This project is a simple backend built with **FastAPI** and **MongoDB**, providing APIs to manage products and user orders. It supports adding products, placing orders, and fetching them with filtering and pagination.

---

## ⚙️ Tech Stack
- **FastAPI** for backend APIs
- **MongoDB** for async database operations
- **Pydantic** for schema validation
- **Uvicorn** as the ASGI server

---

## 📁 Project Structure
├── routes/&ensp;&ensp; # API route handlers <br />
│ ├── products_route.py <br />
│ └── order_route.py <br />
├── utils/ &ensp;&ensp; # DB connection & schema models <br />
│ ├── database.py <br />
│ └── schema.py <br />
├── app.py &ensp;&ensp;# FastAPI app entry point <br/>
├── .env &ensp;&ensp;# MongoDB credentials (ignored in Git)<br/>
├── .gitignore &ensp;&ensp;# Files ignored by Git<br/>
├── render.yaml &ensp;&ensp;# Render deployment config<br/>
├── requirements.txt &ensp;&ensp;# Python dependencies<br/>


## 🌐 API Overview
**POST /api/products** – Add a new product

**GET /api/products** – Get products with optional filters (name, size) and pagination

**POST /api/orders** – Place a new order

**GET /api/orders/{user_id}** – Get orders for a user with product details