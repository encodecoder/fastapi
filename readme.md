## 🎯 Goal

Build a backend service to manage test executions, test suites, failures, analytics, and reports using FastAPI.

By the end of this challenge, you should understand how to:

- Design and build REST APIs.
- Validate data using Pydantic.
- Integrate PostgreSQL using SQLAlchemy.
- Handle asynchronous operations and concurrency.
- Implement authentication and authorization.
- Use Redis for caching.
- Write unit and integration tests.
- Containerize and deploy applications using Docker and Kubernetes.
- Measure API performance and troubleshoot failures.

## 🛠️ Technology Stack

| Area             | Technology             |
| ---------------- | ---------------------- |
| Backend          | Python, FastAPI        |
| Validation       | Pydantic               |
| Database         | PostgreSQL             |
| ORM              | SQLAlchemy             |
| Caching          | Redis                  |
| Authentication   | JWT, OAuth2            |
| Async HTTP       | HTTPX, asyncio         |
| Testing          | Pytest                 |
| Load Testing     | Locust / k6            |
| Containerization | Docker, Docker Compose |
| Orchestration    | Kubernetes             |
| Documentation    | OpenAPI, Swagger       |

---

# 📅 7-Day Roadmap

## Day 1 — FastAPI Fundamentals

**Objective:** Understand how HTTP requests reach your FastAPI application and how APIs are designed.

- Create a Python virtual environment and install FastAPI/Uvicorn.
- Build `GET /health` and `GET /about`.
- Build `GET /test-runs`.
- Implement POST, PUT, PATCH and DELETE.
- Use path and query parameters.
- Implement filtering, sorting and pagination.
- Return appropriate HTTP status codes.
- Explore Swagger UI and OpenAPI.
- Test endpoints using curl.
- Push working code to GitHub.

**Deliverable:** A working CRUD API using in-memory data.

## Day 2 — Pydantic and Application Architecture

**Objective:** Build a clean, maintainable FastAPI application.

- Create `TestRun` and `TestSuite` Pydantic models.
- Use required, optional and default fields.
- Add field validation and constraints.
- Create nested request models.
- Separate routers, schemas and services.
- Implement dependency injection using `Depends()`.
- Create a reusable pagination dependency.
- Add custom exception handling.
- Write tests for invalid payloads.
- Document the request lifecycle.

**Deliverable:** A structured API with reusable components and validated schemas.

## Day 3 — PostgreSQL and SQLAlchemy

**Objective:** Replace in-memory storage with persistent database storage.

- Run PostgreSQL using Docker.
- Connect FastAPI to PostgreSQL.
- Create `test_runs` and `test_suites` tables.
- Learn SQLAlchemy models and sessions.
- Implement database-backed POST endpoint.
- Implement GET by ID and list endpoints.
- Implement update and delete operations.
- Add relationships and foreign keys.
- Handle database errors and transactions.
- Write database integration tests.

**Deliverable:** A database-backed FastAPI application.

## Day 4 — Async Programming and Background Processing

**Objective:** Understand how FastAPI handles concurrent I/O operations.

- Understand `async def` versus `def`.
- Learn `asyncio` and `await`.
- Build an async HTTP endpoint using HTTPX.
- Call multiple APIs concurrently using `asyncio.gather()`.
- Understand blocking I/O.
- Add request timeouts.
- Implement a background report-generation task.
- Create job-status tracking.
- Handle task failures.
- Benchmark concurrent API requests.

**Deliverable:** An API that performs asynchronous external calls and background processing.

## Day 5 — Security and Middleware

**Objective:** Secure your API and understand request processing.

- Implement API-key authentication.
- Implement JWT login and token validation.
- Use password hashing.
- Create admin and viewer roles.
- Protect write endpoints using RBAC.
- Add request-ID middleware.
- Add request logging and timing middleware.
- Implement custom exception handlers.
- Validate authorization on sensitive endpoints.
- Test unauthorized and forbidden requests.

**Deliverable:** A secured API with JWT authentication and role-based authorization.

## Day 6 — Redis, Testing and Performance

**Objective:** Improve API reliability and performance.

- Run Redis using Docker.
- Connect Redis to FastAPI.
- Cache `GET /test-runs`.
- Implement cache invalidation and TTL.
- Add rate limiting.
- Write Pytest unit tests.
- Write API integration tests.
- Test Redis failure handling.
- Load-test with Locust or k6.
- Measure p50, p95 and p99 latency.

**Deliverable:** A tested API with caching and performance measurements.

## Day 7 — Deployment and Final Challenge

**Objective:** Deploy your application like a production backend service.

- Create a production-ready Dockerfile.
- Run API, PostgreSQL and Redis using Docker Compose.
- Configure environment variables and secrets.
- Add health and readiness probes.
- Deploy to a local Kubernetes cluster.
- Configure structured logging.
- Test container restart and recovery.
- Build analytics endpoints for failing and slow suites.
- Write README and architecture diagram.
- Record a demo and publish the project on GitHub.

**Deliverable:** A deployed, production-style FastAPI application.

---

# 🚀 Final Project: Engineering Operations API

Build an API that manages test execution data.

### Required endpoints

| Method | Endpoint              | Purpose                           |
| ------ | --------------------- | --------------------------------- |
| GET    | `/health`             | Service health                    |
| POST   | `/test-runs`          | Ingest a test execution           |
| GET    | `/test-runs`          | Filter, sort and paginate results |
| GET    | `/test-runs/{id}`     | Fetch one execution               |
| GET    | `/analytics/failures` | Find frequently failing suites    |
| GET    | `/analytics/duration` | Find slowest test suites          |
| POST   | `/reports`            | Start report generation           |
| GET    | `/reports/{id}`       | Retrieve report status            |

### Engineering requirements

- FastAPI and Pydantic
- PostgreSQL and SQLAlchemy
- Redis caching
- JWT authentication and role-based access
- Async external API calls
- Pytest unit and integration tests
- Docker Compose
- Kubernetes deployment
- Structured logging and latency measurements

## 📂 Suggested Project Structure

```
engineering-ops-api/
│
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── test_runs.py
│   │   ├── test_suites.py
│   │   ├── analytics.py
│   │   └── reports.py
│   │
│   ├── schemas/
│   ├── models/
│   ├── services/
│   ├── repositories/
│   ├── dependencies/
│   ├── middleware/
│   ├── core/
│   └── database/
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── infrastructure/
│   └── kubernetes/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
```

## 📚 Official Learning Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Redis Documentation](https://redis.io/docs/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)

## 📏 Challenge Rules

1. Spend approximately 3–4 hours daily.
2. Spend 30 minutes learning and the remaining time implementing.
3. Avoid copying complete tutorials.
4. Commit code to GitHub every day.
5. Document one bug or engineering challenge you solved each day.
6. Write tests instead of relying only on manual API calls.
7. Complete the final project independently.

## ✅ Completion Criteria

By the end of seven days, you should be able to independently:

- Design REST APIs.
- Structure a FastAPI application.
- Implement database-backed endpoints.
- Explain synchronous and asynchronous execution.
- Implement authentication and authorization.
- Cache API responses.
- Write automated tests.
- Containerize and deploy your backend.
- Measure and troubleshoot API performance.

**The real test:** Build the final Engineering Operations API without following a step-by-step tutorial. Use official documentation when necessary, and be prepared to explain every architectural decision.

Add daily setup and verification commandsDefine the test-run data contract