# -------------------------------------------
# 📦 Imports
# -------------------------------------------
from flask import Flask
from dotenv import load_dotenv
import os
from datetime import timedelta


# -------------------------------------------
# 🏗️ Flask App Factory
# -------------------------------------------
def create_app():
    """Application factory with enhanced security and session configuration."""

    # Load environment variables
    load_dotenv()

    # Initialize Flask app with custom template folder
    app = Flask(
        __name__, template_folder=_get_template_path(), static_folder=_get_static_path()
    )

    # Configure application
    app.config.update(
        {
            # Security
            "SECRET_KEY": os.getenv("SECRET_KEY", os.urandom(32).hex()),
            "PERMANENT_SESSION_LIFETIME": timedelta(minutes=30),
            # Session
            "SESSION_COOKIE_SECURE": True,  # Only send over HTTPS
            "SESSION_COOKIE_HTTPONLY": True,  # Prevent client-side JS access
            "SESSION_COOKIE_SAMESITE": "Lax",  # CSRF protection
            # File Uploads
            "MAX_CONTENT_LENGTH": 16 * 1024 * 1024,  # 16MB upload limit
        }
    )

    # Register blueprints
    _register_blueprints(app)

    return app


# -------------------------------------------
# 🔧 Helper Functions (Internal)
# -------------------------------------------
def _get_template_path():
    """Get absolute path to templates directory."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates"))


def _get_static_path():
    """Get absolute path to static files directory."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static"))


def _register_blueprints(app):
    """Register application blueprints."""
    from celeb_mind_app.routes import main as main_blueprint

    app.register_blueprint(main_blueprint)
