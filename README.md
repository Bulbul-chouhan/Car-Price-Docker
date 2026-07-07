# 🚗 AI Car Price Prediction System (Dockerized)

A Machine Learning web application that predicts the selling price of a used car based on user inputs. The application is built using **Flask**, **Scikit-learn**, and **Docker**, and is deployed on **Render** for online access.

---

## 🌐 Live Demo

🔗 https://car-price-docker.onrender.com

---

## 📂 GitHub Repository

🔗 https://github.com/Bulbul-chouhan/Car-Price-Docker

---

## 📌 Project Overview

This project predicts the estimated selling price of a used car using a trained Machine Learning model. Users can enter vehicle details through a web interface and instantly receive the predicted car price.

The application has been containerized using Docker and deployed on Render, making it easy to run consistently across different environments.

---

## ✨ Features

- Predicts used car prices instantly
- User-friendly web interface
- Machine Learning model using Scikit-learn
- Dockerized application
- Cloud deployment using Render
- Responsive HTML & CSS frontend

---

## 🛠️ Technologies Used

- Python 3.13
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML5
- CSS3
- Docker
- Git
- GitHub
- Render

---

## 📁 Project Structure

```
Car-Price-Docker/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train.py
├── requirements.txt
├── Dockerfile
├── car_price_model.pkl
├── car data.csv
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Bulbul-chouhan/Car-Price-Docker.git

cd Car-Price-Docker
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open

```
http://localhost:5000
```

---

# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t car-price-app .
```

## Run Docker Container

```bash
docker run -p 10000:10000 car-price-app
```

Open

```
http://localhost:10000
```

---

## 🚀 Deployment

The application is deployed on Render using Docker.

Deployment Steps

- Push project to GitHub
- Connect repository with Render
- Deploy using Docker
- Render automatically builds and hosts the application

Live URL

https://car-price-docker.onrender.com

---

## 📊 Machine Learning Workflow

1. Load Dataset
2. Data Preprocessing
3. Feature Selection
4. Train Regression Model
5. Save Model using Joblib
6. Build Flask Web Application
7. Dockerize the Application
8. Deploy on Render

---

## 📷 Screenshots

### Home Page

(Add Screenshot Here)

### Prediction Result

(Add Screenshot Here)

---

## 👨‍💻 Author

**Bulbul Chouhan**

Integrated M.Tech in Artificial Intelligence

VIT Bhopal University

GitHub

https://github.com/Bulbul-chouhan

---

## ⭐ If you found this project useful, don't forget to star the repository!