# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will build a small RESTful API using the FastAPI framework to learn API design, request/response handling, data validation with Pydantic, and automatic documentation generation.

## 📝 Tasks

### 🛠️ Project Setup

#### Description
Create a minimal FastAPI project with a virtual environment and required dependencies. Provide a `main.py` that mounts the application and a `requirements.txt` listing `fastapi` and `uvicorn`.

#### Requirements

- Include a `requirements.txt` with `fastapi` and `uvicorn` (and optionally `pytest` for tests).
- Provide clear run instructions (e.g., `uvicorn main:app --reload`).

### 🛠️ Implement CRUD Endpoints for a Resource

#### Description
Implement CRUD (Create, Read, Update, Delete) endpoints for a simple resource (for example, `Item` with `id`, `name`, `description`, `price`). Use in-memory storage (a list or dict) — a database is not required for this assignment.

#### Requirements

- Define a Pydantic model for the resource and use it to validate request bodies.
- Implement the following endpoints:
  - `POST /items/` — create an item and return the created item with an assigned `id`.
  - `GET /items/` — return a list of all items.
  - `GET /items/{item_id}` — return a single item or `404` if not found.
  - `PUT /items/{item_id}` — update an item and return the updated item.
  - `DELETE /items/{item_id}` — delete an item and return a 204 or confirmation message.
- Use appropriate status codes and error handling.

### 🛠️ Validation, Query Parameters, and Filtering

#### Description
Add input validation, optional query parameters for filtering/sorting, and demonstrate returning paginated or filtered results.

#### Requirements

- Use Pydantic field types and constraints (e.g., `condecimal`, `conint`, `min_length`).
- Add at least one query parameter (e.g., `min_price`) to filter items returned by `GET /items/`.

### 🛠️ Documentation and Testing

#### Description
Show how to access the automatically generated OpenAPI docs and add a few basic tests for the main endpoints.

#### Requirements

- Document how to open the interactive docs at `/docs` or `/redoc`.
- Provide at least two basic tests using `pytest` (optional: use `httpx` or `TestClient` from `fastapi.testclient`).

## ✅ Expected Outcomes

- A working FastAPI application runnable locally.
- Clear instructions to install dependencies and start the server.
- Properly validated endpoints with Pydantic models and error handling.
- Example requests and responses included below.

## Example Requests & Responses

```
POST /items/
Request body:
{
  "name": "Widget",
  "description": "A small widget",
  "price": 9.99
}

Response 201:
{
  "id": 1,
  "name": "Widget",
  "description": "A small widget",
  "price": 9.99
}

GET /items/?min_price=5.00
Response 200:
[
  {
    "id": 1,
    "name": "Widget",
    "description": "A small widget",
    "price": 9.99
  }
]
```

**Skills practiced:** REST API design, FastAPI basics, Pydantic validation, status codes, and basic testing.
