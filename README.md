# Task Manager

A robust backend API for managing tasks efficiently. Built with FastAPI and PostgreSQL.

## 🛠 Prerequisites

Before running this project, ensure you have the following installed:

* **Python 3.8+**
* **PostgreSQL** (Ensure the service is running)
* **Git**

---

## 🚀 Getting Started

Follow these steps to get your development environment up and running.

### First-Time Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/PranavKumar20/TaskManager.git](https://github.com/PranavKumar20/TaskManager.git)
    cd TaskManager
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    * **Windows:**
        ```bash
        venv\Scripts\activate
        ```
    * **Ubuntu/macOS:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Application:**
    ```bash
    uvicorn app.main:app --reload
    ```

---

### Regular Workflow (Daily Run)

If you have already set up the project, follow these steps to stay updated and run the server:

1.  **Pull latest changes:** `git pull`
2.  **Activate venv:** (See activation commands above)
3.  **Update dependencies:** `pip install -r requirements.txt`
4.  **Launch:** `uvicorn app.main:app --reload`

---

## 🏗 Project Structure

* `app/main.py`: Entry point for the FastAPI application.
* `requirements.txt`: List of Python dependencies.

> **Note:** Ensure your PostgreSQL credentials are correctly configured in your environment variables or configuration file before starting the server.