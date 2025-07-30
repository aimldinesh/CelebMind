# -------------------------------------------
# 📦 Imports
# -------------------------------------------
from celeb_mind_app import create_app
from dotenv import load_dotenv

# -------------------------------------------
# 🚀 App Entry Point
# -------------------------------------------
if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Create Flask app instance
    app = create_app()

    # Run the app on all interfaces at port 5000 with debug mode enabled
    app.run(host="0.0.0.0", port=5000, debug=True)
