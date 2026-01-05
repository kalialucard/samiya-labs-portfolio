---
title: Docker Command List
date: 2026-01-05
category: commands
enrich: false
tags: docker, cybersecurity, command reference, infrastructure
description: Top 10 essential commands for docker.
---

# Docker Command Guide

**Docker** is the standard for containerization.

## Top 10 Useful Commands

### 1. Run Container
```bash
docker run -it ubuntu /bin/bash
```
**Explanation:** Start a container interactively (`-it`).

### 2. List Containers
```bash
docker ps -a
```
**Explanation:** Show all running and stopped containers (`-a`).

### 3. Build Image
```bash
docker build -t myimage .
```
**Explanation:** Build an image from a Dockerfile in current dir.

### 4. Pull Image
```bash
docker pull kalilinux/kali-rolling
```
**Explanation:** Download an image from Docker Hub.

### 5. Remove Container
```bash
docker rm -f <container_id>
```
**Explanation:** Force delete a container.

### 6. Remove Image
```bash
docker rmi <image_id>
```
**Explanation:** Delete an image.

### 7. Exec into Container
```bash
docker exec -it <container_id> /bin/bash
```
**Explanation:** Jump into a running container's shell.

### 8. Logs
```bash
docker logs -f <container_id>
```
**Explanation:** Follow (`-f`) the logs of a container.

### 9. Networks
```bash
docker network ls
```
**Explanation:** List docker networks.

### 10. Prune
```bash
docker system prune -a
```
**Explanation:** Clean up all unused images, containers, and networks.

## The Most Powerful Command
```bash
docker run --rm -it --net=host -v $(pwd):/data kalilinux/kali-rolling bash
```
**Explanation:** instant ephemeral hacking machine with host network access and current folder mounted.

