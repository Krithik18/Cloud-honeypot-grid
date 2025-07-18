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

Deployment
Launch a t3.large EC2 instance with Ubuntu 22.04.

1.Install Docker and Docker Compose:

sudo apt update && sudo apt install -y docker.io docker-compose
sudo usermod -aG docker $USER
newgrp docker

2.Clone this repository and navigate to it:

git clone https://github.com/yourusername/hp-grid.git
cd hp-grid

3.Create persistent folders:

mkdir -p logs/cowrie
mkdir -p filebeat

4.Launch the honeypot grid:

docker-compose up --build

5.Access services:

Fake Web: http://your-ec2-ip:8080
Fake API: http://your-ec2-ip:5000
Kibana Dashboard: http://your-ec2-ip:5601

6.Log Shipping with Filebeat
Filebeat reads Cowrie’s JSON log file and forwards it to Elasticsearch.

Make sure Cowrie is configured to log in JSON format to logs/cowrie/cowrie.json.

Important Notes
1.Increase disk space of the instance to 16GB minimum.
2.Cowrie log file must be at logs/cowrie/cowrie.json for Filebeat to work.
3.This setup uses t3.large for enough memory to run ELK Stack and honeypots.
