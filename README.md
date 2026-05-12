# Linux SRE Debugging Lab

## Overview

This project simulates common Linux and infrastructure failures that Site Reliability Engineers encounter in production environments. The lab was built locally using Docker containers running Linux-based services, with nginx acting as a reverse proxy in front of a FastAPI application.

The goal of this project was to strengthen hands-on Linux troubleshooting skills and practice debugging realistic service failures using common SRE tooling and workflows.

---

# Technologies Used

- Docker
- Docker Compose
- Linux containers
- FastAPI
- nginx
- Python
- curl
- lsof
- ss
- ps
- Docker logs

---

# Scenario 1 — nginx 502 Bad Gateway

## Objective

Simulate a reverse proxy failure where nginx cannot communicate with the backend application.

## Root Cause

nginx was configured to proxy traffic to the wrong upstream port.

## Skills Practiced

- Reverse proxy troubleshooting
- Upstream connectivity debugging
- HTTP status code analysis
- Log analysis
- Container networking

---

# Scenario 2 — Port Already in Use

## Objective

Simulate a service startup failure caused by a port conflict.

## Root Cause

Two services attempted to expose the same host port simultaneously.

## Skills Practiced

- Linux networking fundamentals
- Port binding conflicts
- Process-to-port relationships
- Docker networking concepts

---

# Scenario 3 — Linux Permission Denied

## Objective

Simulate a filesystem permission issue preventing an application from writing logs.

## Root Cause

The mounted log file permissions prevented the application process from writing to the file.

## Skills Practiced

- Linux file permissions
- chmod/chown concepts
- Application logging failures
- Filesystem troubleshooting

---

# Key Linux Commands Practiced

```bash
ps aux
docker ps
docker logs
lsof -i
ss -tulpn
curl -i
ls -l
chmod
whoami
id
```

---

# What I Learned

This project improved my hands-on Linux troubleshooting skills and reinforced common SRE debugging workflows, including:

- Systematic root cause analysis
- Reverse proxy troubleshooting
- Container networking concepts
- Linux permissions and process management
- Log analysis and observability fundamentals

---

# Future Improvements

- Disk full simulation
- CPU and memory exhaustion
- DNS resolution failures
- TLS certificate issues
- Kubernetes deployment debugging