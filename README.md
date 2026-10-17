# TaskBoard DevOps Capstone Project - Comprehensive Documentation

**Student Details:**
* **Name:** Neeshant Ahire
* **Roll Number:** 10635
* **Batch:** A

---

## Table of Contents
1. [Project Overview & Architecture](#1-project-overview--architecture)
2. [Part 1 & 2: Application Creation & Testing (`creation`, `pytest`)](#2-part-1--2-application-creation--testing-creation-pytest)
3. [Part 3: PostgreSQL Database Setup & Schema (`table`)](#3-part-3-postgresql-database-setup--schema-table)
4. [Part 4 & 5: Backend & Frontend Containerization (`backendterm`, `frontendter`, `swagger`)](#4-part-4--5-backend--frontend-containerization-backendterm-frontendter-swagger)
5. [Part 6: CI/CD Pipeline Automation (`cicd`)](#5-part-6-cicd-pipeline-automation-cicd)
6. [Part 7: Container Image Vulnerability Scanning - Trivy (`trivy1`, `trivy2`, `trivy3`)](#6-part-7-container-image-vulnerability-scanning---trivy-trivy1-trivy2-trivy3)
7. [Part 8: Container Registry & Image Management (`registry1`, `registry2`, `registry3`)](#7-part-8-container-registry--image-management-registry1-registry2-registry3)
8. [Part 9 & 10: Infrastructure as Code & Kubernetes Deployment (`helm1`, `helm2`)](#8-part-9--10-infrastructure-as-code--kubernetes-deployment-helm1-helm2)
9. [Part 11: Troubleshooting & Cluster Diagnostics (`troubleshoot`)](#9-part-11-troubleshooting--cluster-diagnostics-troubleshoot)
10. [Part 12: Ingress Routing & Application Access (`ingress`)](#10-part-12-ingress-routing--application-access-ingress)
11. [Part 13: Monitoring & Observability Stack (`prometheus`, `prometheus-term`, `grafana-term`, `grafanan-dash`, `ideal-dash`)](#11-part-13-monitoring--observability-stack-prometheus-prometheus-term-grafana-term-grafanan-dash-ideal-dash)
12. [Project Presentation Link](#12-project-presentation-link)

---

## 1. Project Overview & Architecture
The **TaskBoard** capstone project is an enterprise-grade, microservices-based task management platform built to demonstrate advanced DevOps principles. It integrates containerization, automated testing, continuous integration pipelines, infrastructure vulnerability scanning, declarative Kubernetes orchestration via Helm charts, horizontal autoscaling, Ingress routing, and a full Prometheus/Grafana observability stack deployed on a local Minikube cluster.

---

## 2. Part 1 & 2: Application Creation & Testing (`creation`, `pytest`)
- **Application Logic:** Developed modular FastAPI backend endpoints paired with a responsive frontend interface.
- **Automated Testing:** Executed `pytest` suites to validate application logic, unit tests, and database connectivity prior to building production container images.
![Ideal Dashboard View](screenshots/ideal-dash.png)
![Creation Screenshot](screenshots/creation.png)
![Pytest Screenshot](screenshots/pytest.png)

---

## 3. Part 3: PostgreSQL Database Setup & Schema (`table`)
- **Database Provisioning:** Deployed a PostgreSQL stateful container inside the `taskboard` Kubernetes namespace.
- **Manual Verification & Schema Configuration:** Accessed the active PostgreSQL pod via `kubectl exec` and created the core `tasks` table with fields for unique identification, title, description, and status (`todo`, `in_progress`, `completed`), inserting sample testing records.

```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50) DEFAULT 'todo'
);
INSERT INTO tasks (title, description, status) VALUES ('Complete Capstone Project', 'Finish final demo requirements', 'in_progress');
```

![Database Table Screenshot](screenshots/table.png)

---

## 4. Part 4 & 5: Backend & Frontend Containerization (`backendterm`, `frontendter`, `swagger`)
- **Container Build Process:** Authored production-ready multi-stage `Dockerfile` configurations for both backend (`taskboard_assignment-backend:latest`) and frontend (`taskboard_assignment-frontend:latest`) services.
- **API Documentation:** Verified interactive API schemas via FastAPI's built-in Swagger UI (`/docs`).

![Backend Terminal Screenshot](screenshots/backendterm.png)
![Frontend Terminal Screenshot](screenshots/frontendter.png)
![Swagger UI Screenshot](screenshots/swagger.png)

---

## 5. Part 6: CI/CD Pipeline Automation (`cicd`)
- **Pipeline Implementation:** Configured automated workflows to handle build verification, code linting, and artifact pushing on code check-ins.

![CI/CD Pipeline Screenshot](screenshots/cicd.png)

---

## 6. Part 7: Container Image Vulnerability Scanning - Trivy (`trivy1`, `trivy2`, `trivy3`)
- **Security Audit:** Installed and executed `trivy` container image scans on local build artifacts to detect OS package vulnerabilities and embedded secrets.
- **Execution Command:**
  ```bash
  trivy image taskboard_assignment-backend:latest
  ```

![Trivy Scan 1](screenshots/trivy1.png)
![Trivy Scan 2](screenshots/trivy2.png)
![Trivy Scan 3](screenshots/trivy3.png)

---

## 7. Part 8: Container Registry & Image Management (`registry1`, `registry2`, `registry3`)
- **Registry Push:** Authenticated with Docker Hub and pushed tagged repository images (`taskboard_assignment_backend` and `taskboard_assignment_frontend`).
- **Verification:** Confirmed repository availability and tag visibility directly via container registry dashboards.

![Registry 1](screenshots/registry1.png)
![Registry 2](screenshots/registry2.png)
![Registry 3](screenshots/registry3.png)

---

## 8. Part 9 & 10: Infrastructure as Code & Kubernetes Deployment (`helm1`, `helm2`)
- **Infrastructure Provisioning:** Utilized Terraform modules to define cloud infrastructure requirements.
- **Helm Orchestration:** Packaged Kubernetes manifests into a modular Helm chart (`./helm/taskboard`) and deployed the stack into the `taskboard` namespace using `helm upgrade --install`.

![Helm Deployment 1](screenshots/helm1.png)
![Helm Deployment 2](screenshots/helm2.png)

---

## 9. Part 11: Troubleshooting & Cluster Diagnostics (`troubleshoot`)
- **Debugging & Error Resolution:** Resolved container image pull backoffs, namespace mapping mismatches, and database socket connection blocks (`FATAL: role "postgres" does not exist` resolved by shifting to user `-U taskboard`).

![Troubleshooting Screenshot](screenshots/troubleshoot.png)

---

## 10. Part 12: Ingress Routing & Application Access (`ingress`)
- **Traffic Management:** Configured Kubernetes Ingress rules and local port-forwarding fallbacks to route external HTTP traffic successfully to internal application services.

![Ingress Screenshot](screenshots/ingress.png)

---

## 11. Part 13: Monitoring & Observability Stack (`prometheus`, `prometheus-term`, `grafana-term`, `grafanan-dash`, `ideal-dash`)
- **Prometheus & Grafana:** Deployed the `kube-prometheus-stack` Helm chart into the `monitoring` namespace.
- **Image Pull Resolution:** Overcame Quay.io upstream pull rate limits by pre-pulling images locally and loading them into Minikube via `minikube image load`.
- **Target Verification:** Port-forwarded Prometheus to port `9090`, validated active target scrapes, and imported Grafana custom operational dashboards.

![Prometheus UI](screenshots/prometheus.png)
![Prometheus Terminal](screenshots/prometheus-term.png)
![Grafana Terminal](screenshots/grafana-term.png)
![Grafana Dashboard](screenshots/grafanan-dash.png)


---

## 12. Project Presentation Link
* **Local Presentation File:** [TaskBoard_Capstone_Presentation.pptx](./demo/TaskBoard-DevOps-Capstone.pptx)