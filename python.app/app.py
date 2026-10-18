
from flask import Flask
from routes import register_routes


def create_app(testing=False):
    """Membuat dan mengatur aplikasi Flask."""
    app = Flask(__name__)
    app.config["TESTING"] = testing

    register_routes(app)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
