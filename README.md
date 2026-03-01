# TechPulse - AI Tools & Tech News Portal

A Django-based web application that provides information about AI tools and latest tech news.

## Features

- **AI Tools Directory**: Browse and search AI tools with filtering options
- **Tech News Aggregator**: Latest news about AI and technology
- **Dual View Types**: Both Function-Based Views (FBV) and Class-Based Views (CBV)
- **Advanced Filtering**: Search by tool name, category, trending status, news source
- **Admin Interface**: Full CRUD operations for managing tools and news
- **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

- Python 
- Django 
- SQLite (development) / MySQL (production)
- HTML5/CSS3
- Virtual Environment

STEP 1: Clone the repository
git clone https://github.com/YOUR_USERNAME/techpulse.git
cd techpulse

STEP 2: Create and activate virtual environment
For macOS/Linux:
python3 -m venv venv
source venv/bin/activate

For Windows:
python -m venv venv
venv\Scripts\activate

STEP 3: Install dependencies
pip install -r requirements.txt

STEP 4: Apply database migrations
python manage.py makemigrations tools
python manage.py makemigrations news
python manage.py migrate

STEP 5: Create superuser
python manage.py createsuperuser
(Follow the prompts to set username, email, and password)

STEP 6: Load sample data (optional)
python populate_data.py

STEP 7: Run development server
python manage.py runserver

STEP 8: Access the application
Open your browser and go to:
http://127.0.0.1:8000/tools/
http://127.0.0.1:8000/admin/

STEP 9: To stop the server
Press Control + C in the terminal
