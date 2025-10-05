#!/bin/bash
# Student Performance Analytics - Installation Script

echo "Setting up Student Performance Analytics System..."

# Create virtual environment
python -m venv venv
echo "Virtual environment created."

# Activate virtual environment
if [[ "$OSTYPE" == "msys" ]]; then
    # Windows
    source venv/Scripts/activate
else
    # Linux/Mac
    source venv/bin/activate
fi

echo "Virtual environment activated."

# Install dependencies
pip install -r requirements.txt
echo "Dependencies installed."

# Run migrations
python manage.py makemigrations
python manage.py migrate
echo "Database migrations completed."

# Create superuser (optional)
echo "To create admin user, run: python manage.py createsuperuser"

# Start development server
echo "Setup completed!"
echo "To start the server, run: python manage.py runserver"
echo "Then visit: http://127.0.0.1:8000"
