## 🚀 Deployment Setup Instructions

### ✅ Pre-Deployment Checklist

Make sure the following components are ready:

- ✅ Dockerfile  
- ✅ Kubernetes Deployment file  
- ✅ Code Versioning using GitHub

---

### ✅ Enable Required GCP APIs

Go to **GCP Console** → **APIs & Services** → **Library**, and enable:

- Kubernetes Engine API  
- Container Registry API  
- Compute Engine API  
- Cloud Build API  
- Cloud Storage API  
- IAM API

---

### ✅ Create GKE Cluster and Artifact Registry

1. **Create GKE Cluster:**
   - In GCP Console, search for **GKE**.
   - Create a new cluster.
   - Configure networking and access as needed.

2. **Create Artifact Registry:**
   - In GCP Console, search for **Artifact Registry**.
   - Create a new registry.

---

### ✅ Create a Service Account and Configure Access

1. **Create Service Account** in GCP Console.

2. **Assign Roles:**
   - Storage Object Admin  
   - Storage Object Viewer  
   - Owner  
   - Artifact Registry Admin  
   - Artifact Registry Writer  

3. **Download the key** as `.json` (e.g., `gcp-key.json`).

4. **Place the key** in your project root.

5. **Add to `.gitignore`:**

   ```bash
   gcp-key.json
   ```
### 🔐 Convert gcp-key.json to Base64
```bash
cat gcp-key.json | base64 -w 0
```
- Use the output in CircleCI secrets/environment variables.

### ✅ Set Up CircleCI Configuration
1. Create CircleCI config file at:
```bash
.circleci/config.yml
```
2. Connect CircleCI to GitHub.
3. Ensure config file is detected.

### ✅ Add Environment Variables in CircleCI
Navigate to Project Settings → Environment Variables, and add:
- GCLOUD_SERVICE_KEY — Base64 GCP key
- GOOGLE_PROJECT_ID — GCP project ID
- GKE_CLUSTER — Cluster name
- GOOGLE_COMPUTE_REGION — Compute region

### ✅ Set Up LLMOps Secrets in GKE
1. Authenticate kubectl with GKE:
```bash
gcloud container clusters get-credentials llmops-cluster1 \
--region us-central1 \
--project your-project-id
```
2. Create Kubernetes secret:
```bash
kubectl create secret generic llmops-secrets \
--from-literal=GROQ_API_KEY="your_actual_groq_api_key"
```

### ✅ Trigger CircleCI Pipeline
- Manually trigger your pipeline from CircleCI dashboard.
- Future deployments will be automatically triggered on every git push.