# IT Services Django Project

## Description
This is a web application built using the Django framework, designed to provide various IT services. It features a home page and is structured to allow for easy expansion of services and functionalities.

## Features
*   Homepage displaying an overview of IT services.
*   Modular Django application structure (`itservice` app).
*   Utilizes SQLite as the default database.

## Technologies Used
*   Python
*   Django
*   SQLite

## Setup/Installation

### Prerequisites
*   Python 3.x installed on your system.

### Steps
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Vinayakp2001/aqua-service
    cd personal
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (optional, for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create your superuser.

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be accessible at `http://127.0.0.1:8000/`.

## Project Structure
*   `personal/`: The root directory of the Django project.
*   `personal/itservices/`: The main Django project configuration.
    *   `settings.py`: Project settings.
    *   `urls.py`: Main URL routing for the project.
*   `personal/itservice/`: A Django application handling core IT service functionalities.
    *   `models.py`: Database models for the `itservice` app.
    *   `views.py`: Logic for handling web requests and returning responses.
    *   `urls.py`: URL routing specific to the `itservice` app.
    *   `templates/itservice/home.html`: The main template for the homepage.
*   `db.sqlite3`: The SQLite database file.
*   `requirements.txt`: Lists all Python dependencies.
*   `manage.py`: Django's command-line utility for administrative tasks.

## Usage
After running the development server, navigate to `http://127.0.0.1:8000/` in your web browser to access the IT Services application.

## License
[License Name or "MIT License" if you prefer, or remove this section if not applicable.]
