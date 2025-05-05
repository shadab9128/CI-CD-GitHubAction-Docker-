# 🔁 Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible

Automatically detect service failures and recover them using alerts and automation tools like Prometheus, Alertmanager, and Ansible.

---

## 📌 Objective

Implement a self-healing mechanism for containerized services (like NGINX) by:
- Monitoring service uptime with Prometheus
- Triggering alerts using Alertmanager
- Executing Ansible playbooks via webhook to restart failed services

---

## 🧰 Tech Stack

- [x] Prometheus – Monitoring system
- [x] Alertmanager – Alert handling and routing
- [x] Ansible – Task automation
- [x] Shell Scripting
- [x] Docker & Docker Compose
- [x] Flask (Python) – Webhook listener

---


---

## 🚀 How It Works

1. **NGINX** runs as a sample service.
2. **Prometheus** scrapes NGINX metrics.
3. If NGINX is down (`up == 0`), Prometheus triggers an alert.
4. **Alertmanager** receives the alert and routes it to a **custom webhook**.
5. Webhook runs an **Ansible playbook** to restart the NGINX container.
6. The system heals itself.

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/Self-Healing-Infra.git
cd Self-Healing-Infra
```
### 2. Start Docker Daemon

```bash
sudo systemctl start docker
```
### 3. Build and Run All Services

```bash
docker-compose up --build -d
```

### 4. Access Services
NGINX: http://localhost:8080

Prometheus: http://localhost:9090

Alertmanager: http://localhost:9093

Webhook (Flask): http://localhost:5001

### Screenshots 
- All the screenshots is given in Screenshot Folder

## 🤝 Contribution
Feel free to fork, contribute, and enhance the self-healing capabilities (e.g., CPU/memory monitoring, auto-scaling, service mesh integration).