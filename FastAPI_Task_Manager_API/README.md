# Task Manager API

A modern, RESTful Task Management API built with FastAPI. This application provides a complete CRUD (Create, Read, Update, Delete) interface for managing tasks with features like priority levels, due dates, and task completion tracking.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Request & Response Examples](#request--response-examples)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Create Tasks**: Add new tasks with title, description, priority, and due dates
- **Read Tasks**: Retrieve all tasks or specific task by ID with filtering options
- **Update Tasks**: Modify existing tasks with partial or full updates
- **Delete Tasks**: Remove tasks from the database
- **Task Filtering**: Filter tasks by completion status
- **Pagination**: Support for pagination with skip and limit parameters
- **Priority Levels**: Tasks can have priority levels from 1-5
- **Data Validation**: Pydantic-based validation for all request payloads
- **Status Codes**: Proper HTTP status codes for all operations
- **Interactive Documentation**: Auto-generated Swagger UI and ReDoc documentation

## 🛠 Tech Stack

- **FastAPI**: 0.136.1+ - Modern async web framework
- **Pydantic**: 2.13.4+ - Data validation and serialization
- **Uvicorn**: 0.47.0+ - ASGI server
- **Python**: 3.12+

## 📁 Project Structure

```
task_manager_api/
├── main.py                 # Entry point
├── requirements.txt        # Project dependencies
├── pyproject.toml         # Project configuration
├── README.md              # Documentation
└── app/
    ├── main.py            # FastAPI app initialization
    ├── database/
    │   └── db.py          # In-memory database (task_db list)
    ├── routers/
    │   └── task_router.py # Task API routes and endpoints
    ├── schema/
    │   └── task_schema.py # Pydantic models for validation
    └── services/
        └── task_services.py # Business logic for task operations
```

## 🚀 Installation

### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Steps

1. **Clone the repository** (or navigate to the project directory)
   ```bash
   cd task_manager_api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or using pyproject.toml:
   ```bash
   pip install -e .
   ```

## 💻 Usage

### Running the Application

Start the development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

**Available Endpoints:**
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## 📡 API Endpoints

All endpoints are prefixed with `/tasks`

### 1. Create a Task
- **Endpoint**: `POST /tasks/`
- **Status Code**: `201 Created`
- **Description**: Create a new task

### 2. Get All Tasks
- **Endpoint**: `GET /tasks/`
- **Status Code**: `200 OK`
- **Description**: Retrieve all tasks with optional filtering and pagination
- **Query Parameters**:
  - `skip` (int): Number of tasks to skip (default: 0)
  - `limit` (int): Maximum number of tasks to return (default: 10, max: 100)
  - `completed` (bool, optional): Filter by completion status

### 3. Get Task by ID
- **Endpoint**: `GET /tasks/{task_id}`
- **Status Code**: `200 OK` or `404 Not Found`
- **Description**: Retrieve a specific task by its ID

### 4. Update Task
- **Endpoint**: `PUT /tasks/{task_id}`
- **Status Code**: `200 OK` or `404 Not Found`
- **Description**: Update an existing task (partial or full update)

### 5. Delete Task
- **Endpoint**: `DELETE /tasks/{task_id}`
- **Status Code**: `204 No Content` or `404 Not Found`
- **Description**: Delete a task by its ID

## 📦 Request & Response Examples

### Create a Task
**Request:**
```bash
curl -X POST "http://127.0.0.1:8000/tasks/" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project documentation",
    "description": "Write comprehensive API documentation",
    "priority": 4,
    "due_date": "2026-06-15",
    "completed": false
  }'
```

**Response (201 Created):**
```json
{
  "id": 1,
  "title": "Complete project documentation",
  "description": "Write comprehensive API documentation",
  "priority": 4,
  "due_date": "2026-06-15",
  "completed": false
}
```

### Get All Tasks
**Request:**
```bash
curl -X GET "http://127.0.0.1:8000/tasks/?skip=0&limit=10"
```

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "title": "Complete project documentation",
    "description": "Write comprehensive API documentation",
    "priority": 4,
    "due_date": "2026-06-15",
    "completed": false
  },
  {
    "id": 2,
    "title": "Test API endpoints",
    "description": "Verify all endpoints work correctly",
    "priority": 3,
    "due_date": "2026-06-10",
    "completed": false
  }
]
```

### Get Task by ID
**Request:**
```bash
curl -X GET "http://127.0.0.1:8000/tasks/1"
```

**Response (200 OK):**
```json
{
  "id": 1,
  "title": "Complete project documentation",
  "description": "Write comprehensive API documentation",
  "priority": 4,
  "due_date": "2026-06-15",
  "completed": false
}
```

**Error Response (404 Not Found):**
```json
{
  "detail": "Task not found"
}
```

### Update Task
**Request:**
```bash
curl -X PUT "http://127.0.0.1:8000/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{
    "completed": true,
    "priority": 5
  }'
```

**Response (200 OK):**
```json
{
  "id": 1,
  "title": "Complete project documentation",
  "description": "Write comprehensive API documentation",
  "priority": 5,
  "due_date": "2026-06-15",
  "completed": true
}
```

### Delete Task
**Request:**
```bash
curl -X DELETE "http://127.0.0.1:8000/tasks/1"
```

**Response (204 No Content):** No response body

### Filter Tasks by Completion Status
**Request:**
```bash
curl -X GET "http://127.0.0.1:8000/tasks/?completed=false&skip=0&limit=20"
```

## 📝 Task Model Schema

### TaskCreate / TaskBase
```json
{
  "title": "string (required, 3-100 characters)",
  "description": "string (optional, max 100 characters)",
  "completed": "boolean (default: false)",
  "due_date": "date (optional, format: YYYY-MM-DD)",
  "priority": "integer (required, 1-5)"
}
```

### TaskUpdate
All fields are optional for partial updates:
```json
{
  "title": "string (optional, 3-100 characters)",
  "description": "string (optional, max 100 characters)",
  "completed": "boolean (optional)",
  "due_date": "date (optional, format: YYYY-MM-DD)",
  "priority": "integer (optional, 1-5)"
}
```

### TaskResponse
```json
{
  "id": "integer (auto-generated)",
  "title": "string",
  "description": "string or null",
  "completed": "boolean",
  "due_date": "date or null",
  "priority": "integer"
}
```

## 🔍 Validation Rules

- **Title**: Required, minimum 3 characters, maximum 100 characters
- **Description**: Optional, maximum 100 characters
- **Priority**: Required for creation, must be between 1 (lowest) and 5 (highest)
- **Due Date**: Optional, format must be valid date (YYYY-MM-DD)
- **Completed**: Boolean flag indicating task completion status
- **Skip/Limit**: Must be non-negative, limit cannot exceed 100

## 📊 Key Features Explained

### Pagination
Tasks can be retrieved with pagination using `skip` and `limit` parameters:
- `skip`: Number of records to skip (useful for pagination)
- `limit`: Maximum records to return (default 10, max 100)

### Filtering
Get completed or incomplete tasks:
```bash
# Get all completed tasks
curl -X GET "http://127.0.0.1:8000/tasks/?completed=true"

# Get all incomplete tasks
curl -X GET "http://127.0.0.1:8000/tasks/?completed=false"
```

### Partial Updates
Update only specific fields without affecting others:
```bash
# Update only the priority
curl -X PUT "http://127.0.0.1:8000/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{"priority": 2}'
```

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---
