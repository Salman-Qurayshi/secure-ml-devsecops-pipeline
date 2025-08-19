# 🔐 Secure ML DevSecOps Pipeline

Hello there 👋, this is my end-to-end ML DevSecOps project: I trained a model and made it accessible via a REST API, then containerized and secured it with a CI/CD pipeline.

I wanted to not just train a model, but also treat it like real production software: **containerize it, scan it, and deploy it through a secure CI/CD pipeline.**

---

## 🔹 Project Overview
- **ML Model → Flask API** (Iris dataset)
- **Containerized with Docker**
- **Automated CI/CD pipeline with Jenkins**
- **Security-first approach: linting, SAST, image scanning**

---

## ⚙️ Features
✅ Trained ML model served via Flask  
✅ Dockerized for consistent deployment  
✅ Automated Jenkins pipeline  
✅ Security integrations:
- Flake8 + Black (Linting & formatting)
- Bandit (Static Application Security Testing - SAST)
- Trivy (Container vulnerability scanning)
- (Optional) GitLeaks for secret scanning 🔑

---

## 🔄 CI/CD Pipeline Stages
1. **Linting** → Flake8 + Black  
2. **Static code analysis** → Bandit  
3. **Unit tests** → Ensure API + model work  
4. **Docker build & push** → Build image and push to registry  
5. **Trivy image scan** → Security check on the container  
6. **Deployment** → Run model API in container  

---

## 🔐 Security in Action
- **Bandit** checking my Python code for vulnerabilities  
- **Trivy** scanning my Docker image for CVEs  
- (Optional) **GitLeaks** can be added to prevent secret leaks  

---

## 📦 Model Serving
The final container runs the **model API**:

```bash
docker run -p 5000:5000 ml-api:latest
