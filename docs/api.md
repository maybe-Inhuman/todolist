<div align="center">

# API Documentation

Everything you need to talk to the ToDo list over HTTP: simple JSON endpoints, no auth, ready to try with `curl`.

</div>

## Overview

| Method | Path      | Description                |
| ------ | --------- | -------------------------- |
| GET    | `/`       | Greeting message           |
| GET    | `/health` | Application health check   |

- **Base URL:** `http://127.0.0.1:8000`
- **Format:** all responses are JSON (`application/json`)
- **Authentication:** not required

## Running the server

```bash
uv run python server.py
```

Interactive documentation is generated automatically:

- Swagger UI: `/docs`
- ReDoc: `/redoc`
- OpenAPI schema: `/openapi.json`

## Endpoints

### 1. Root

```http
GET /
```

Returns a greeting message.

**Example**

```bash
curl http://127.0.0.1:8000/
```

**Response** `200 OK`

```json
{
  "message": "Hello World"
}
```

### 2. Health

```http
GET /health
```

Checks that the application is running. Suitable for liveness probes.

**Example**

```bash
curl http://127.0.0.1:8000/health
```

**Response** `200 OK`

```json
{
  "status": "ok"
}
```

## Errors

Errors are returned as JSON with a `detail` field.

| Status | Meaning                                  |
| ------ | ---------------------------------------- |
| 404    | Endpoint not found                       |
| 405    | HTTP method is not allowed for this path |

```json
{
  "detail": "Not Found"
}
```
