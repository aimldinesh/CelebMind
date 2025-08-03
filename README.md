<p align="center">
  <img src="https://img.shields.io/github/last-commit/aimldinesh/CelebMind" alt="Last Commit Badge">
  <img src="https://img.shields.io/badge/deployed-GCP-brightgreen" alt="Deployment Badge">
  <img src="https://img.shields.io/badge/LLM-LLaMA_4-red" alt="LLM Badge">
  <img src="https://img.shields.io/github/stars/aimldinesh/CelebMind?style=social" alt="GitHub Stars">
  <br><br>
  <img src="https://img.shields.io/badge/Docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Badge"/>
  <img src="https://img.shields.io/badge/OpenCV-27338e?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV Badge"/>
  <img src="https://img.shields.io/badge/Flask-000000.svg?style=for-the-badge&logo=flask&logoColor=white" alt="Flask Badge"/>
  <img src="https://img.shields.io/badge/Kubernetes-326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes Badge"/>
</p>



<h1 align="center">🎬 CelebMind: Celebrity Detector & Q&A App</h1>

<p align="center">
  An intelligent AI app that <strong>detects celebrities from uploaded images</strong> and answers user queries about them using <strong>Groq's Llama 3 LLM</strong>. Built with <strong>OpenCV</strong>, <strong>Flask</strong>, and <strong>Kubernetes</strong> for scalable deployment.
</p>

---
## 📚 Table of Contents

1. [🎬 Project Overview](#-celebmind-celebrity-detector--qa-app)
2. [📌 Features](#-features)
3. [🧱 Architecture](#-architecture)
4. [🔄 Project Workflow](#-project-workflow)
5. [🔄 Step-By-Step : How it works?](#-step-by-step--how-it-works)
6. [🧪 Tech Stack](#-tech-stack)
7. [🚀 Setup Instructions](#-setup-instructions)
8. [✅ Docker Run (Optional)](#-docker-run-optional)
9. [🚀 Deployment Setup Instructions](#-deployment-setup-instructions)
10. [📸 Sample Output](#-sample-output)
    - [🧠 CelebMind App UI](#-celebmind-app-ui)
    - [⚙️ CircleCI Pipeline](#️-circleci-pipeline)
    - [☁️ GCP Deployment](#️-gcp-deployment)
11. [📚 Future Improvements](#-future-improvements)
12. [💡 Credits](#-credits)
13. [🤝 Contributors](#-contributors)

---

## 📌 Features

- 🧠 **LLM-Powered Q&A**: Asks questions about the detected celebrity using Groq's Llama 3 model.
- 🧍‍♂️ **Celebrity Detection**: Uses OpenCV to detect and identify celebrities from uploaded photos.
- 🚀 **Real-time Inference**: Instant answers from LLM served via Flask API.
- 📦 **Dockerized Microservice**: Containerized and deployable across any environment.
- ☸️ **Kubernetes Ready**: GKE deployment with CircleCI for CI/CD.
- 🔒 **Secure & Lightweight**: Environment variable support with `.env` and optimized image.

---

## 🧱 Architecture

```mermaid
graph TD
    A[User Uploads Image] --> B[Flask Backend]
    B --> C[OpenCV: Celebrity Detection]
    B --> D[Groq API Call for LLM Answer]
    C --> E[Detected Celebrity Name]
    D --> F[Answer to Question]
    E --> G[Display Response on UI]
    F --> G
```

## 🔄 Project Workflow
```mermaid
graph TD
    A[🧑 User Uploads Image] --> B[🖼️ Flask Backend Receives Image]
    B --> C[🧠 OpenCV Face Detection + Matching]
    C --> D[✅ Celebrity Identified]

    D --> E[📝 User Enters Question]
    E --> F[🧩 Prompt Construction]
    F --> G[🚀 Groq LLaMA 3.1-70B API Call]

    G --> H[💡 LLM Generates Answer]
    H --> I[🌐 Flask Sends Response]
    I --> J[🖥️ Frontend Displays Result]

    J --> K[🔁 CircleCI CI/CD Pipeline]
    K --> L[🐳 Docker Build & Push to GCP Registry]
    L --> M[Kubernetes Deploy to GKE]

```
## 🔄 Step-By-Step : How it works?

The **CelebMind** project follows a streamlined workflow to deliver fast, intelligent celebrity detection and Q&A using LLMs:

---

### 1. 🖼️ User Uploads an Image
- The user provides an image via the frontend interface.
- The image is sent to the Flask backend API.

---

### 2. 🧠 Celebrity Detection (OpenCV)
- The backend uses **OpenCV** to analyze facial features.
- It matches the image with a pre-defined celebrity dataset (embeddings or templates).
- If a match is found, the **celebrity's name is extracted**.

---

### 3. ❓ User Submits a Question
- The user types a **natural-language question** related to the celebrity.
- The question and the detected celebrity name are **combined into a single prompt**.

---

### 4. ⚡ Groq LLM API (LLaMA 3.1 70B)
- The composed prompt is sent to **Groq's ultra-fast inference API** using the `llama3-70b-qa` model.
- The model generates an **intelligent and context-aware answer**.

---

### 5. 🛠️ Flask Response Rendering
- The LLM response is sent back to the Flask server.
- Flask renders the result along with:
  - The detected image
  - The celebrity name

---

### 6. 💻 Frontend Display
The UI displays:
- ✅ Detected celebrity photo and name  
- ✅ User's original question  
- ✅ LLM-generated answer  

---

### 7. 🚀 CI/CD & Deployment
- Code is pushed to **GitHub**
- **CircleCI pipeline**:
  - Builds Docker image
  - Pushes image to **GCP Artifact Registry**
  - Deploys to **Google Kubernetes Engine (GKE)** using `kubectl`

---

## 🧪 Tech Stack
| Area       | Tools & Frameworks               |
| ---------- | -------------------------------- |
| Backend    | Flask, Python                    |
| Frontend   | HTML/CSS, JS (simple templating) |
| ML / AI    | OpenCV, Groq API (LLaMA-3.1 70B) |
| Deployment | Docker, Kubernetes (GKE)         |
| CI/CD      | CircleCI, GitHub                 |
| Infra      | GCP VM, GKE, Container Registry  |

---
## 🚀 Setup Instructions
### 1️⃣ Clone the repo
```bash
git clone https://github.com/aimldinesh/celebmind.git
cd celebmind
```
### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3️⃣ Install dependencies
```bash
pip install -e .
```
### 4️⃣ Set environment variables
Create a .env file:
```bash
GROQ_API_KEY = ""
```
### 5. Run locally
```bash
python app.py
```
The app will be available at: http://127.0.0.1:5000

---
## ✅ Docker Run (Optional)
```bash
docker build -t celebmind-app .
docker run -p 5000:5000 celebmind-app
```
---

## 🚀 Deployment Setup Instructions
For detailed, end-to-end deployment steps including GCP setup, Kubernetes configuration, and CircleCI integration:

👉 [View Setup Instructions →](./setup_instruction.md)

## 📸 Sample Output

### 🧠 CelebMind App UI

| Image Upload                                                                                                                           | Celebrity Detection + Q&A                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Upload Image 1](https://github.com/aimldinesh/CelebMind/blob/main/screenshots/App_images/1.App_image_Celebrity_image_1_upload.PNG)  | ![Response 1](https://github.com/aimldinesh/CelebMind/blob/main/screenshots/App_images/2.App_image_detect_celebrity_name_and_info_QA_response.PNG) |
| ![Upload Image 2](https://github.com/aimldinesh/CelebMind/blob/main/screenshots/App_images/3.App_image__Celebrity_image_2_upload.PNG) | ![Response 2](https://github.com/aimldinesh/CelebMind/blob/main/screenshots/App_images/4.App_image_detect_celebrity_name_and_info_QA_response.PNG) |

---

### ⚙️ CircleCI Pipeline

| Homepage                                                                                                     | Trigger                                                                                                             |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| ![CircleCI Homepage](https://github.com/aimldinesh/CelebMind/blob/main/screenshots/circleci/1.homepage.png) | ![Pipeline Trigger](https://github.com/aimldinesh/CelebMind/blob/main/screenshots/circleci/2.circleci_trigger.png) |

| Build Success                                                                                                                | Project Summary                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| ![Pipeline Success](https://github.com/aimldinesh/CelebMind/blob/main/screenshots/circleci/3.circleci_pipeline_success.PNG) | ![Project Success](https://github.com/aimldinesh/CelebMind/blob/main/screenshots/circleci/4.circleci_project_success.PNG) |

---

### ☁️ GCP Deployment

![App Deployed on GCP](https://github.com/aimldinesh/CelebMind/blob/main/screenshots/app_deployed_gcp/celebmind_app_deployed_on_GCP.png)

---
## 📚 Future Improvements

- ✅ **Add multiple celebrity support**  
- ✅ **Enhance UI styling**  
- 🔜 **Add Redis caching for Q&A**  
- 🔜 **Integrate voice-based question input**

---
## 💡 Credits
- Groq API (LLaMA 3)
- OpenCV for computer vision
- Flask for backend
- Kubernetes on GKE

---
## 🤝 Contributors
- [Dinesh](https://github.com/aimldinesh)

