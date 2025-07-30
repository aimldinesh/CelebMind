# -------------------------------------------
# 📦 Imports
# -------------------------------------------
from flask import Blueprint, render_template, request, session
import base64
from datetime import datetime

from celeb_mind_app.utils.image_handler import process_image
from celeb_mind_app.utils.celebrity_detector import CelebrityDetector
from celeb_mind_app.utils.celebrity_qa import QAEngine

# -------------------------------------------
# 🔧 Flask Blueprint Setup
# -------------------------------------------
main = Blueprint("main", __name__)

# Initialize the Celebrity Detection and QA modules
celebrity_detector = CelebrityDetector()
qa_engine = QAEngine()


# -------------------------------------------
# 🧠 Main Route: Handles Image Upload & QA
# -------------------------------------------
@main.route("/", methods=["GET", "POST"])
def index():
    # Initialize from session
    context = {
        "celebrity_info": session.get("celebrity_info", ""),
        "result_img_data": session.get("result_img_data", ""),
        "celebrity_name": session.get("celebrity_name", ""),
        "user_question": "",
        "answer": "",
        "now": datetime.now(),
    }

    if request.method == "POST":
        # Handle image upload
        if "image" in request.files and request.files["image"]:
            session.clear()
            img_bytes, face_box = process_image(request.files["image"])

            if face_box is not None:
                context["celebrity_info"], _ = celebrity_detector.identify(img_bytes)
                context["result_img_data"] = base64.b64encode(img_bytes).decode()

                # Extract name safely
                name = "Unknown Celebrity"
                if context["celebrity_info"]:
                    lines = context["celebrity_info"].splitlines()
                    if lines and ":" in lines[0]:
                        name = lines[0].split(":", 1)[-1].strip()

                context["celebrity_name"] = name
                session.update(context)
            else:
                context["celebrity_info"] = (
                    "No face detected. Please try another image."
                )
                session.update(context)

        # Handle QA submissions
        elif "question" in request.form:
            context.update(
                {
                    "user_question": request.form.get("question", ""),
                    "celebrity_name": request.form.get("celebrity_name", ""),
                    "celebrity_info": request.form.get("celebrity_info", ""),
                    "result_img_data": request.form.get("result_img_data", ""),
                }
            )

            if context["user_question"]:
                context["answer"] = qa_engine.ask_about_celebrity(
                    context["celebrity_name"], context["user_question"]
                )

            # Update session with current state
            session.update(context)

    return render_template("index.html", **context)
