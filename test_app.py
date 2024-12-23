# test_app.py
from flask import Flask
import pytest

# Create a simple Flask app
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

# Test case for the Flask app
def test_hello():
    with app.test_client() as client:
        response = client.get('/')
        assert response.data == b"Hello, World!"
