# Backend: 
FastAPI for managing books and users
This backend exposes REST endpoints for adding, searching, borrowing books, and managing users.

# Frontend: 
Streamlit interagissant avec FastAPI

# Create aws infrastructure:
We will create some aws services to host the application.

1. Create aws Security group for EC2.



# Clone or donwload the project:

```
git clone https...
```

# Create python virtualenv:

```
cd aws-library-project

python -m venv venv

or 

python3 -m venv venv

```

## Activate the virtualenv

```
.\venv\Scripts\activate

ou 

source venv/bin/activate 
```

# Install the dependencies:

```
pip install -r requierements.txt

or 

pip3 install -r requirements.txt
```
# Test the applicaiton localy

## Launch the backend:

Open a terminal and run this command:

```
uvicorn backend:app --reload
```
visite this url **http://127.0.0.1:8000/docs**

## Launch the Frontend:

Open a terminal and run this command:

```
streamlit run frontend.py
```
Visite this url **http://localhost:8501/**