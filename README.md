# Aqua Services IT Solutions

## Description
This is a modern, responsive web application built using the Django framework, designed to provide various IT services. The frontend has been completely redesigned to offer a sleek and engaging user experience, inspired by the aesthetic of `growlect.com`.

## Features
*   **Modern & Responsive UI:** A clean, visually appealing, and fully responsive user interface.
*   **Dynamic Homepage:** Displays an overview of IT services with dynamic, image-rich service cards.
*   **Interactive Hero Section:** Features an engaging video background.
*   **Dedicated Pages:** Includes Home, Services (dynamic detail pages), About, Contact, and an Admin Dashboard.
*   Modular Django application structure (`itservice` app).
*   Utilizes SQLite as the default database.

## Technologies Used
*   Python
*   Django
*   HTML5
*   CSS3 (with modern techniques like Flexbox, Grid, custom properties)
*   JavaScript (for UI/UX enhancements like mobile menu toggle, scroll effects)
*   Font Awesome (for icons)
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

4.  **Create Static Directories and Add Media Files:**
    Manually create the necessary static directories and place your media files:
    ```bash
    mkdir -p itservice/static/images
    mkdir -p itservice/static/video
    ```
    Place your `.jpg` image files (e.g., `service-webdev.jpg`, `project-creative.jpg`, `about-us-main.jpg`, `favicon.ico`) into `itservice/static/images/`.
    Place your `.mp4` video files (e.g., `hero-background.mp4`) into `itservice/static/video/`.
    Ensure the filenames match those referenced in `itservice/views.py` and `itservice/templates/itservice/home.html`.

5.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser (optional, for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create your superuser.

7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be accessible at `http://127.0.0.1:8000/`.

## Project Structure
*   `personal/`: The root directory of the Django project.
*   `personal/itservices/`: The main Django project configuration.
    *   `settings.py`: Project settings (updated for static files).
    *   `urls.py`: Main URL routing for the project (includes static file serving).
*   `personal/itservice/`: A Django application handling core IT service functionalities.
    *   `models.py`: Database models for the `itservice` app.
    *   `views.py`: Logic for handling web requests, returning responses, and passing dynamic data (e.g., service images).
    *   `urls.py`: URL routing specific to the `itservice` app.
    *   `templates/itservice/`: Contains all HTML templates.
        *   `home.html`: The redesigned homepage template.
        *   `service_detail.html`: Template for individual service detail pages (with dynamic background images).
        *   `about.html`: About Us page template.
        *   `contact.html`: Contact Us page template.
        *   `dashboard.html`: Admin Dashboard template.
    *   `static/`: Directory for static assets.
        *   `css/style.css`: Global styles for the website.
        *   `css/service_detail.css`: Page-specific styles for service detail pages.
        *   `images/`: Directory for various images (e.g., service cards, project images, favicon).
        *   `video/`: Directory for background videos.
*   `db.sqlite3`: The SQLite database file.
*   `requirements.txt`: Lists all Python dependencies.
*   `manage.py`: Django's command-line utility for administrative tasks.

## Frontend Design Principles
The frontend design is inspired by `growlect.com`, focusing on:
*   **Clean & Modern Aesthetic:** A sleek, professional look with a user-friendly interface.
*   **Responsive Layout:** Adapts seamlessly to various screen sizes (desktop, tablet, mobile).
*   **Prominent Hero Section:** Engaging visual introduction with video background.
*   **Clear Sectioning:** Well-defined and visually distinct sections for easy navigation.
*   **Consistent Typography & Color Palette:** Ensures a cohesive brand identity.
*   **Interactive Elements:** Subtle animations and hover effects to enhance user engagement.

## Usage
After running the development server, navigate to `http://127.0.0.1:8000/` in your web browser to access the Aqua Services application.

## License
[License Name or "MIT License" if you prefer, or remove this section if not applicable.]

