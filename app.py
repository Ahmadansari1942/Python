from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import platform
import random

app = Flask(__name__)

# ─────────────────────────────────────────
#  App Config
# ─────────────────────────────────────────

app.config['APP_NAME'] = "Ahmad's Flask App"
app.config['APP_VERSION'] = "1.0.0"
app.config['AUTHOR'] = "Ahmad"

# Simple in-memory store (no DB needed for now)
visitors = 0
messages = []

motivational_quotes = [
    "Code is like humor. When you have to explain it, it's bad.",
    "First, solve the problem. Then, write the code.",
    "Experience is the name everyone gives to their mistakes.",
    "The best error message is the one that never shows up.",
    "Simplicity is the soul of efficiency.",
]

# ─────────────────────────────────────────
#  Helper Functions
# ─────────────────────────────────────────

def get_server_info():
    """Returns basic server/system info."""
    return {
        "python_version": platform.python_version(),
        "system": platform.system(),
        "machine": platform.machine(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

def count_visitor():
    """Increments visitor counter."""
    global visitors
    visitors += 1
    return visitors

# ─────────────────────────────────────────
#  Page Routes
# ─────────────────────────────────────────

@app.route('/')
def home():
    count_visitor()
    quote = random.choice(motivational_quotes)
    return render_template('index.html', quote=quote, visitors=visitors)

@app.route('/about')
def about():
    info = get_server_info()
    return render_template('about.html', info=info, version=app.config['APP_VERSION'])

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        message = request.form.get('message', '').strip()
        if name and message:
            messages.append({
                "name": name,
                "message": message,
                "time": datetime.now().strftime("%H:%M:%S")
            })
        return redirect(url_for('contact'))
    return render_template('contact.html', messages=messages)

@app.route('/dashboard')
def dashboard():
    stats = {
        "visitors": visitors,
        "messages": len(messages),
        "uptime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "version": app.config['APP_VERSION'],
    }
    return render_template('dashboard.html', stats=stats)

# ─────────────────────────────────────────
#  API Routes
# ─────────────────────────────────────────

@app.route('/api/hello')
def api_hello():
    return jsonify({
        "message": "Hello from Flask API!",
        "status": "success",
        "author": app.config['AUTHOR'],
        "version": app.config['APP_VERSION'],
    })

@app.route('/api/status')
def api_status():
    info = get_server_info()
    return jsonify({
        "status": "running",
        "visitors": visitors,
        "messages_count": len(messages),
        "server": info,
    })

@app.route('/api/quote')
def api_quote():
    return jsonify({
        "quote": random.choice(motivational_quotes),
        "status": "success",
    })

@app.route('/api/messages')
def api_messages():
    return jsonify({
        "messages": messages,
        "total": len(messages),
    })

# ─────────────────────────────────────────
#  Error Handlers
# ─────────────────────────────────────────

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error", "status": 500}), 500

# ─────────────────────────────────────────
#  Run
# ─────────────────────────────────────────

if __name__ == '__main__':
    print(f"Starting {app.config['APP_NAME']} v{app.config['APP_VERSION']}")
    print(f"Author: {app.config['AUTHOR']}")
    print("Running on http://0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)