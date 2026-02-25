# Ahmad's Flask App

A simple Python Flask web application. Clean, minimal, ready for GitHub and CI/CD deployment.

## Structure

```
flask-app/
├── app.py
├── requirements.txt
└── templates/
    ├── index.html
    └── about.html
```

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

App runs on `http://localhost:5000`

## Routes

- `/` — Home page
- `/about` — About page  
- `/api/hello` — JSON API endpoint
