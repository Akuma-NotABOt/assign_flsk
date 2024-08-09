# assign_flsk

## 🌟 Overview
This repository showcases a minimal yet functional Flask application, designed for seamless deployment via Docker. It's perfect for developers looking to quickly spin up a web app within a containerized environment, ensuring consistency across different systems.

## 🚀 Features
- **Flask Framework**: Lightweight and flexible web application using Flask.
- **Dockerized**: Simplified deployment with Docker, including `docker-compose` for orchestration.
- **Dependency Management**: Python packages neatly organized in `requirements.txt`.

## 🛠️ Getting Started

### Prerequisites
- **Docker**: Ensure Docker is installed and running.
- **Docker Compose**: Required for multi-container Docker applications.

### Installation & Setup
1. **Clone the Repo**:
    ```bash
    git clone https://github.com/Akuma-NotABOt/assign_flsk.git
    ```
2. **Navigate** to the project directory:
    ```bash
    cd assign_flsk
    ```
3. **Build & Run** using Docker Compose:
    ```bash
    docker-compose up --build
    ```
   This command builds the Docker image and runs the application in a container.

## 🌐 Accessing the Application
Once the container is up, you can interact with the Flask application by sending HTTP requests to `http://localhost:5000` using tools like `curl`, Postman, or through your frontend code.
