# Cloud-honeypot-grid

This project sets up a Docker-based honeypot grid on AWS using Cowrie (SSH), a fake web server, and a fake API service. All container logs are centrally shipped to the ELK Stack (Elasticsearch, Logstash, Kibana) using Filebeat for analysis and threat detection.

## Objectives

- Monitor unauthorized access attempts in real-time
- Simulate attack surfaces for ethical threat intelligence
- Analyze logs using Kibana dashboards

---

## Features

- Cowrie honeypot for SSH/Telnet deception
- Custom fake web and API services (HTTP/Flask)
- Log shipping using Filebeat
- Real-time visualization with Kibana
- AWS EC2-based, low-cost deployment

---

## Avoiding Common Pitfalls

> These were fixed based on real deployment errors:

- **Disk Space**: EC2 volume set to **16 GB minimum**
- **t2.micro too slow**: Use at least **t3.large (8GB RAM)** for smooth operation
- **Kibana stuck**: Wait 3–5 minutes after launching; it needs time to initialize
- **Cowrie logs not visible**: Ensure volumes and permissions are correctly mounted
- **Filebeat not logging**: Use container paths `/var/lib/docker/containers` + enable Docker socket

---

## Quick Start

### Step 1: Launch AWS EC2 (Ubuntu 22.04)

- Instance type: `t3.large`
- Storage: at least `16 GB`
- Security Group: allow ports `22`, `2222`, `80`, `5000`, `5601`, `9200`

### Step 2: Install Docker & Docker Compose

```bash
sudo apt update
sudo apt install docker.io docker-compose -y
