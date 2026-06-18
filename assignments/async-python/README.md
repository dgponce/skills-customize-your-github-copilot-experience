# 📘 Assignment: Async Programming with asyncio

## 🎯 Objective

Introduce asynchronous programming in Python using `asyncio` to write non-blocking code and manage concurrent tasks.

## 📝 Tasks

### 🛠️ Write asynchronous functions

#### Description
Implement a set of `async` functions that perform simulated I/O-bound work (use `asyncio.sleep`) and coordinate them with `asyncio.gather` and `asyncio.create_task`.

#### Requirements

- Demonstrate `async def` functions and `await` usage.
- Run multiple tasks concurrently and collect results.
- Use `asyncio` task cancellation in at least one scenario.

### 🛠️ Apply timeouts and error handling

#### Description
Add timeouts and proper exception handling for tasks.

#### Requirements

- Use `asyncio.wait_for` to enforce a timeout for a task.
- Handle cancellations and exceptions gracefully.

**Skills practiced:** Coroutines, event loop, concurrency primitives, and error handling.
