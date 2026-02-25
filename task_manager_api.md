# 🧠 Task Manager API (FastAPI)

## 📌 Features

### 👤 User Management

-   Create user
-   Get user by ID
-   Get all users
-   Delete user
-   Update user 

### 🔐 Authentication (later phase)

-   User login
-   JWT token generation
-   Protected routes
-   Password hashing (bcrypt)

### 📝 Task Management

-   Create task
-   Get task by ID
-   Get all tasks
-   Get tasks by user
-   Update task
-   Delete task

### 🔗 Relationships

-   One user → many tasks
-   Each task belongs to one user

### ⚙️ Advanced (later phase)

-   Pagination (limit, offset)
-   Filtering (status, priority)
-   Sorting (created_at, due_date)
-   Soft delete (optional)
-   Logging
-   Exception handling
-   Environment-based config

------------------------------------------------------------------------

## 🚀 API Endpoints

### 👤 User APIs

#### ✅ Create User

POST /api/v1/users/

#### ✅ Get All Users

GET /api/v1/users/

#### ✅ Get User By ID

GET /api/v1/users/{user_id}

#### ✅ Delete User

DELETE /api/v1/users/{user_id}

#### ✅ Update User

PUT /api/v1/users/{user_id}

------------------------------------------------------------------------

### 🔐 Auth APIs (Later)

#### ⏳ Register

POST /api/v1/auth/register

#### ⏳ Login

POST /api/v1/auth/login

#### ⏳ Get Current User

GET /api/v1/auth/me

------------------------------------------------------------------------

### 📝 Task APIs

#### ⏳ Create Task

POST /api/v1/tasks/

#### ⏳ Get All Tasks

GET /api/v1/tasks/

#### ⏳ Get Task By ID

GET /api/v1/tasks/{task_id}

#### ⏳ Get Tasks By User

GET /api/v1/tasks/user/{user_id}

#### ⏳ Update Task

PUT /api/v1/tasks/{task_id}

#### ⏳ Delete Task

DELETE /api/v1/tasks/{task_id}

------------------------------------------------------------------------

## 📊 Status Legend

-   ✅ Implemented
-   ⏳ Pending

------------------------------------------------------------------------

## 🧱 Tech Stack

-   FastAPI
-   PostgreSQL
-   SQLAlchemy
-   Alembic
-   Pydantic
