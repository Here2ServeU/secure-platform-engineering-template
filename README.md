# Secure Platform Engineering Template

This project helps teams set up a secure, reliable, and automated system to manage cloud platforms (AWS, Azure, GCP) using GitOps, Kubernetes, Backstage, and Infrastructure as Code. Ideal for teams in regulated industries like healthcare, finance, and education.

---

## Project Structure

```plaintext
secure-platform-engineering-template/
├── ai-tools/
│   ├── config-validator.py          # AI tool to validate Terraform configs
│   ├── log-summarizer.py            # AI tool to summarize log files
│   └── requirements.txt             # Python dependencies for AI tools
│
├── backstage/
│   ├── manifests/                   # Kubernetes YAMLs for Backstage + PostgreSQL
│   ├── terraform/                   # Terraform configs for Backstage infrastructure
│   ├── terragrunt/                  # Terragrunt environment configs for cloud provisioning
│   ├── catalog-info.yaml            # Backstage component metadata
│   ├── Dockerfile                   # Dockerfile to containerize Backstage app
│   ├── README.md                    # Backstage-specific documentation
│   └── template.yaml                # Backstage software template for new services
│
├── ci-cd/                           # CI/CD pipeline definitions (GitHub, GitLab, Jenkins)
│
├── kubernetes/                      # Core platform manifests (Vault, ArgoCD, OPA, etc.)
│
├── observability/                   # OpenTelemetry, Prometheus, and Grafana config
│
└── README.md                        # Root-level documentation
```

---

## What This Project Does

- Automates cloud infrastructure provisioning (no manual setup)
- Installs developer tools like Backstage
- Ensures security and compliance with Vault and OPA
- Provides full observability through Grafana and Prometheus
- Uses AI to help with log summaries, cost insights, and configuration validation

---

## How to Use the AI Tools

### Purpose

The AI tools allow you to:
- **Summarize noisy logs** using GPT models for faster debugging
- **Validate Terraform configs** for misconfigurations or security gaps
- **Predict costs** and suggest optimizations using FinOps modeling

### Setup

```bash
cd ai-tools
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run the Tools

```bash
# Summarize logs
python log-summarizer.py --file ../logs/app.log

# Validate Terraform configurations
python config-validator.py --path ../terraform/aws

# Generate cost insights
python finops-analyzer.py --usage ../billing/aws.csv
```

---

## How to Use This (Simple Instructions)

1. Choose your cloud: AWS, GCP, or Azure
2. Navigate to the appropriate environment folder:
```bash
cd terragrunt/aws/dev         # or gcp/dev, azure/dev
terragrunt apply
```

3. Deploy platform tools to Kubernetes:
```bash
cd kubernetes/manifests
kubectl apply -f .
```

4. Access your services:
- Backstage: `https://backstage.example.com`
- Vault: `https://vault.example.com`
- Grafana: `https://grafana.example.com`

---

## Local Deployment (Backstage Only)

### Prerequisites:
- Docker
- Node.js >= v18
- Yarn
- Kind or Minikube
- kubectl

### Steps:

1. Clone and start:
```bash
git clone https://github.com/Here2ServeU/secure-platform-engineering-template.git
cd secure-platform-engineering-template/backstage
yarn install
yarn dev
```

Backstage will be accessible at: `http://localhost:7007`

---

## Cloud Deployment (Backstage and Services)

### Prerequisites:
- Terraform and Terragrunt
- AWS CLI, Azure CLI, or gcloud
- kubectl
- Docker image pushed to a container registry

### Provision Kubernetes Infrastructure:

AWS:
```bash
cd backstage/terragrunt/aws/dev
terragrunt apply
```

Azure:
```bash
cd backstage/terragrunt/azure/dev
terragrunt apply
```

GCP:
```bash
cd backstage/terragrunt/gcp/dev
terragrunt apply
```

### Deploy Kubernetes Manifests:
```bash
cd backstage/manifests
kubectl apply -f postgres-storage.yaml
kubectl apply -f postgres.yaml
kubectl apply -f postgres-service.yaml
kubectl apply -f backstage-secrets.yaml
kubectl apply -f backstage.yaml
kubectl apply -f backstage-service.yaml
```

---

## Configuration Example

`app-config.yaml`
```yaml
app:
  baseUrl: http://localhost

organization:
  name: Spotify

backend:
  baseUrl: http://localhost
  listen:
    port: 7007
  cors:
    origin: http://localhost
  database:
    client: pg
    connection:
      host: ${POSTGRES_HOST}
      port: ${POSTGRES_PORT}
      user: ${POSTGRES_USER}
      password: ${POSTGRES_PASSWORD}
```

---

## Clean Up

```bash
kubectl delete namespace backstage
# or
cd backstage/terragrunt/aws/dev
terragrunt destroy
```

---

## Who Should Use This

- Startups scaling into cloud infrastructure
- Teams prioritizing automation, compliance, and observability
- DevOps teams in healthcare, finance, and SaaS industries

---

## Contact

Created by: Emmanuel Naweji  
LinkedIn: https://www.linkedin.com/in/ready2assist  
GitHub: https://github.com/Here2ServeU  
Medium: https://medium.com/@here2serveyou
