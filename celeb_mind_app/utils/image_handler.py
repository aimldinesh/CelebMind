import cv2
from io import BytesIO
import numpy as np
from typing import Tuple, Optional


def process_image(
    image_file,
) -> Tuple[Optional[bytes], Optional[Tuple[int, int, int, int]]]:
    """
    Process the uploaded image:
    - Converts image to OpenCV format.
    - Detects the largest face using Haar cascades.
    - Draws a bounding box on the largest detected face.
    - Returns the processed image bytes and face coordinates.

    Args:
        image_file: The uploaded image file from the frontend (e.g., Flask request.files).

    Returns:
        Tuple:
            - Processed image bytes (with bounding box if face is found),
            - Coordinates of the largest face as (x, y, w, h), or None if no face is found.
    """

    # Convert uploaded image file to in-memory byte stream
    in_memory_file = BytesIO()
    image_file.save(in_memory_file)
    image_bytes = in_memory_file.getvalue()

    # Convert bytes to numpy array for OpenCV processing
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert image to grayscale (required for face detection)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load OpenCV's pre-trained Haar Cascade for frontal face detection
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # If no face detected, return original image bytes and None for face
    if len(faces) == 0:
        return image_bytes, None

    # Select the largest face by area (width * height)
    largest_face = max(faces, key=lambda r: r[2] * r[3])
    (x, y, w, h) = largest_face

    # Draw a green bounding box around the largest face
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Encode the modified image back to bytes (JPEG format)
    is_success, buffer = cv2.imencode(".jpg", img)

    # Handle encoding failure
    if not is_success:
        return None, largest_face

    # Return processed image bytes and largest face coordinates
    return buffer.tobytes(), largest_face
