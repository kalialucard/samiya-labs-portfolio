---
title: Kubernetes Command List
date: 2026-01-05
category: commands
enrich: false
tags: kubernetes, cybersecurity, command reference
description: Top 10 essential commands for kubernetes.
---

# Kubernetes (kubectl) Command Guide

**Kubernetes** is the standard for orchestration.

## Top 10 Useful Commands

### 1. Get Pods
```bash
kubectl get pods -A
```
**Explanation:** List pods in all namespaces.

### 2. Describe
```bash
kubectl describe pod <pod_name>
```
**Explanation:** Show detailed status/events for a pod.

### 3. Logs
```bash
kubectl logs -f <pod_name>
```
**Explanation:** Follow logs.

### 4. Exec
```bash
kubectl exec -it <pod_name> -- /bin/bash
```
**Explanation:** Shell access to a pod.

### 5. Apply YAML
```bash
kubectl apply -f deployment.yaml
```
**Explanation:** Create/Update resources from file.

### 6. Delete
```bash
kubectl delete pod <pod_name>
```
**Explanation:** Remove a pod (k8s usually restarts it).

### 7. Get Services
```bash
kubectl get svc
```
**Explanation:** List networking services.

### 8. Scale
```bash
kubectl scale deployment/myapp --replicas=3
```
**Explanation:** Manually scale instances.

### 9. Port Forward
```bash
kubectl port-forward <pod_name> 8080:80
```
**Explanation:** Access internal pod port 80 via local 8080.

### 10. Cluster Info
```bash
kubectl cluster-info
```
**Explanation:** Check master/dns status.

## The Most Powerful Command
```bash
kubectl auth can-i --list
```
**Explanation:** Check your RBAC privileges to see if you can escalate rights or delete system components.

