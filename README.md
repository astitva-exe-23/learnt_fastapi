
# FastAPI Task Management API

This is a simple task management API built using FastAPI. It allows you to perform CRUD (Create, Read, Update, Delete) operations on tasks. Each task has an ID, a title, an optional description, and a completion status.

## Features

- **Create a Task**: Add a new task with a unique ID.
- **Read Tasks**: Retrieve all tasks or a specific task by its ID.
- **Update a Task**: Modify the details of an existing task.
- **Delete a Task**: Remove a task by its ID.

## Requirements

- Python 3.7 or later
- FastAPI
- Uvicorn
- Pydantic

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install fastapi uvicorn pydantic
   ```

## Running the Application

To start the FastAPI server, run the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Replace `main` with the name of your Python file if it's different.

## API Endpoints

### Create a Task

- **URL**: `/tasks/`
- **Method**: `POST`
- **Request Body**: 
  ```json
  {
    "title": "Task Title",
    "description": "Optional description",
    "completed": false
  }
  ```
- **Response**: The created task with an assigned `id`.

### Get All Tasks

- **URL**: `/tasks/`
- **Method**: `GET`
- **Response**: A list of all tasks.

### Get a Task by ID

- **URL**: `/tasks/{task_id}`
- **Method**: `GET`
- **Response**: The task with the specified `task_id`. Returns a 404 error if not found.

### Update a Task

- **URL**: `/tasks/{task_id}`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "title": "Updated Title",
    "description": "Updated description",
    "completed": true
  }
  ```
- **Response**: The updated task. Returns a 404 error if the task is not found.

### Delete a Task

- **URL**: `/tasks/{task_id}`
- **Method**: `DELETE`
- **Response**: The deleted task. Returns a 404 error if the task is not found.

## Example

To test the API, you can use tools like `curl`, `httpie`, or Postman. Here is an example using `httpie` to create a task:

```bash
http POST http://localhost:8000/tasks/ title="Sample Task" description="This is a sample task"
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

