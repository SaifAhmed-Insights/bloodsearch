# 🩸 Blood Donation Platform

A web application built using **Django** to help users register and find blood donors based on blood group and location.

## Features

- User Registration with:
  - Name
  - Email
  - Blood Group
  - Phone Number
  - Location
- Admin dashboard
- Secure form handling with CSRF protection
- Clean and responsive registration page

## 🛠 Tech Stack

- **Backend**: Django (Python)
- **Database**: SQLite (can be replaced with MySQL or PostgreSQL)
- **Frontend**: HTML, CSS (Bootstrap optional)

##  Installation Guide

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/blood-donation.git
   cd blood-donation
2. Create a virtual environment
    python -m venv venv
source venv/Scripts/activate  # On Windows

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py makemigrations
python manage.py migrate

5. Run the development server
python manage.py runserver

6. Visit http://127.0.0.1:8000 in your browser.

 Configuration

    Ensure SECRET_KEY, DEBUG, and DATABASES are properly set in settings.py.

    If using MySQL or PostgreSQL, update the database configuration accordingly.

 To Do

    Add donor search functionality

    Implement user login/authentication

    Add email/SMS notifications

 License

This project is licensed under the MIT License. See the LICENSE file for more information.

 Contact

Saif Ahmed
📧 saifahmed.insights@gmail.com
📍 New York, USA
📱 +1 (929) 346-2598
