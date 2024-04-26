# API
Creating a simple crud api

# How to run the app
git clone https://github.com/Rockson95/API.git

# Navigat to the project directory
C:\Users\stage\api_app>

# Installing fast api
pip install fastapi

# Set Up the Virtual Environment
python -m venv venv

# Activate the Virtual Environment
.\venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Run the API
uvicorn app:app --reload

# Access the API
http://127.0.0.1:8000/

# Testing Endpoints
http://127.0.0.1:8000/races/


# Virtual environment

The app runs on both env and venv. It gives OSError when you use one.

# Testind Endpoint with specific year (Get)
http://127.0.0.1:8000/race/1912

# Testind Endpoint with specific year (Delete)
http://127.0.0.1:8000/race/1912

# I used postman to test it.

# Deactivate the Virtual Environment
CRT+C OR Type deactivate


