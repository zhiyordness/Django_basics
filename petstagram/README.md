# Petstagram

Petstagram is a Django-based web application inspired by Instagram, but exclusively for pets! Users can create profiles for their pets, upload photos, and interact with other pet photos by leaving comments and likes.

## Features

*   **User Authentication:** Register, login, and logout functionality for users.
*   **Profile Management:** Create, view, edit, and delete user profiles.
*   **Pet Management:** Add, view, edit, and delete pet profiles.
*   **Photo Uploads:** Upload photos of your pets, including a description and location.
*   **Tagging:** Tag one or more pets in a photo.
*   **Engagement:** Like and comment on photos.

## Technologies Used

*   **Backend:** Python, Django
*   **Database:** PostgreSQL
*   **Image Handling:** Pillow
*   **Environment Variables:** python-dotenv

## Setup and Installation

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   Python 3.9+
*   PostgreSQL

### Installation

1.  **Clone the repository:**
    ```sh
    git clone <your-repository-url>
    cd petstagram
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    python -m venv .venv
    source .venv/bin/activate
    # On Windows, use: .venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up the environment variables:**

    Create a `.env` file in the project root directory. This file will hold your secret key and database credentials. Copy the example below and replace the placeholder values with your actual credentials.

    ```.env
    # Django
    SECRET_KEY='your-super-secret-key'

    # PostgreSQL Database
    DB_NAME='petstagram_db'
    DB_USER='your_db_user'
    DB_PASS='your_db_password'
    DB_HOST='localhost'
    DB_PORT='5432'
    ```

5.  **Run database migrations:**
    ```sh
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`.

## Project Structure

The project is organized into several Django apps:

*   `accounts/`: Handles user registration, authentication, and profiles.
*   `pets/`: Manages the creation and details of pets.
*   `photos/`: Manages photo uploads, details, editing, and deletion.
*   `common/`: Contains shared functionality like the home page, comments, and likes.
*   `static/`: Contains static files (CSS, images).
*   `templates/`: Contains the HTML templates for the application.
