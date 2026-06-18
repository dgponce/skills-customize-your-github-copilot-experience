# 📘 Assignment: API Testing & TDD with FastAPI

## 🎯 Objective

Teach test-driven development for REST APIs by building a small FastAPI service and writing unit and integration tests with `pytest` and `TestClient`.

## 📝 Tasks

### 🛠️ Initialize the project (TDD first)

#### Description
Start by writing failing tests for a small FastAPI app (an `Item` resource) before implementing the endpoints. Use `pytest` and FastAPI's `TestClient`.

#### Requirements

- Provide a `requirements.txt` including `fastapi`, `uvicorn`, `pytest`, and `httpx`.
- Add `tests/` with at least two failing tests before implementation.

### 🛠️ Implement CRUD endpoints (pass tests)

#### Description
Implement endpoints for `POST /items/`, `GET /items/`, `GET /items/{id}`, `PUT /items/{id}`, and `DELETE /items/{id}` so tests pass.

#### Requirements

- Use Pydantic models for request/response validation.
- Use in-memory storage (dict/list) for items.
- Return appropriate status codes and JSON responses.

### 🛠️ Add test coverage and edge cases

#### Description
Extend tests to cover validation errors, not-found cases, and idempotency where appropriate.

#### Requirements

- Include parameterized tests and fixtures in `tests/`.
- Demonstrate mocking or isolated tests if needed.

## ✅ Expected Outcomes

- A FastAPI app that can be run locally with `uvicorn`.
- A test suite runnable with `pytest` that demonstrates TDD workflow.
- Instructions to run server and tests.

## Example commands

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn starter-code:app --reload
pytest -q
```
