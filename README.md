# Secure Platform Engineering Template – Emmanuel Services Edition

Welcome to the **Secure Platform Engineering Template** — a complete open-source solution that helps you build a secure, highly available, and developer-friendly cloud infrastructure.

This project makes it easy to launch production-grade platforms in the cloud using Kubernetes and modern DevOps tools. The goal? Help developers **focus only on building software**, not setting up infrastructure.

---

## What This Project Includes

```plaintext
secure-platform-engineering-template/
├── ai-tools/                  # AI tools for logs and cost analysis
│   ├── log-summarizer.py
│   └── finops-analyzer.py
│
├── infrastructure/           # Infrastructure-as-Code to provision Kubernetes clusters
│   ├── terraform/            # Base Terraform files for AWS, Azure, and GCP
│   └── terragrunt/           # Environment-aware wrappers for Terraform
│
├── backstage/                # Developer portal setup using Backstage on Kubernetes
│   └── manifests/            # K8s YAMLs for Backstage, Postgres, Services
│
├── scripts/                  # Helper scripts
│   ├── cleanup.sh            # Remove Docker, K8s, and IaC artifacts
│   └── vpc-subnet-id-generator.sh  # AWS VPC/Subnet utility
│
├── logs/                     # Directory for storing logs to analyze with AI tools
│   └── app.log
│
├── requirements.txt          # Python dependencies for AI tools
└── README.md                 # This documentation
```

---

## Why This is the Most Secure and Developer-Friendly Platform

- Built with security-first components: **Vault**, **OPA Gatekeeper**, and encrypted secrets
- Compliance-ready: meets **HIPAA**, **SOC 2**, **PCI**, **HITRUST**, **FedRAMP**
- Hosted on **Kubernetes**, the gold standard for scalability and container orchestration
- Integrated with **Backstage**, a developer portal that simplifies discovery, deployment, and documentation
- Uses **AI** to help teams detect log issues and forecast costs intelligently

---

## Non-Technical Summary: What Does This Do?

- It sets up a secure cloud environment automatically (no manual clicks needed)
- It gives developers a web interface (Backstage) where they can:
  - Launch services
  - View documentation
  - Deploy apps
  - Track logs and metrics
- It uses automation tools to keep things **secure, reproducible, and scalable**

---

## Getting Started

### Step 1: Clone the Project
```bash
git clone https://github.com/Here2ServeU/secure-platform-engineering-template.git
cd secure-platform-engineering-template
```

### Step 2: Set Up Infrastructure
Choose your cloud:
```bash
cd infrastructure/terragrunt/aws/dev         # or azure/dev, gcp/dev
terragrunt apply
```

This will create:
- A managed Kubernetes cluster (EKS, AKS, or GKE)
- Networking resources (VPCs, subnets)
- Storage and secrets support


---

### Step 3: Configure Kubernetes Access on Your Local Machine

After provisioning your Kubernetes cluster with Terragrunt, you need to set up your local machine to connect to it using `kubectl`.

#### For AWS (EKS)
```bash
aws eks --region <your-region> update-kubeconfig --name <your-cluster-name>
```

#### For Azure (AKS)
```bash
az aks get-credentials --resource-group <your-resource-group> --name <your-cluster-name>
```

#### For Google Cloud (GKE)
```bash
gcloud container clusters get-credentials <your-cluster-name> --region <your-region> --project <your-project-id>
```

Once configured, verify with:
```bash
kubectl get nodes
```

You should see the list of cluster nodes. You're now ready to deploy workloads to your cloud Kubernetes cluster from your local machine.

---

## Deploy Developer Platform

### Step 1: Apply Kubernetes Resources
```bash
cd backstage/manifests
kubectl apply -f .
```

This installs:
- Backstage (developer portal)
- PostgreSQL (database for Backstage)
- Kubernetes services and secrets

### Step 2: Access Backstage
```bash
kubectl get svc -n backstage
```

Look for the `EXTERNAL-IP` of the `backstage` service. Visit it in your browser:
```
http://<EXTERNAL-IP>
```

---

## Developer Experience

Backstage will greet your team with:
- **Emmanuel Services** as the first microservice template
- Tools to create, catalog, and deploy services
- Golden paths to standardize best practices

No need to learn YAML, Kubernetes, or Terraform — developers click and code.

---

## AI Tools Included

### 1. Log Summarization
```bash
python ai-tools/log-summarizer.py logs/app.log
```

This scans your logs and highlights errors, warnings, and critical issues.

### 2. FinOps Cost Forecasting
```bash
python ai-tools/finops-analyzer.py ai-tools/sample-billing.csv
```

This estimates your monthly/annual cloud costs and identifies top spend areas.

### Requirements:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Full Cleanup

To remove everything and reset:
```bash
bash scripts/cleanup.sh
```

This deletes:
- Docker leftovers
- Terraform and Terragrunt state
- Kubernetes configs
- Cached files and logs

---

## Why This Platform Works

| Feature                  | Benefit to Your Team |
|--------------------------|----------------------|
| Backstage IDP            | One interface to manage all services |
| ArgoCD + GitOps          | Safer, automated deployments |
| Vault + OPA              | Secrets management & compliance enforcement |
| Kubernetes + Terraform   | Auto-healing, scalable, cloud-agnostic setup |
| Terragrunt               | Reuse infra logic across dev, stage, prod |
| AI Tools                 | Faster issue detection and better cost control |

---

## Questions or Help?

- **LinkedIn**: [ready2assist](https://www.linkedin.com/in/ready2assist)
- **GitHub**: [Here2ServeU](https://github.com/Here2ServeU)

---

This project was built to help **developers build faster, safer, and smarter** — without worrying about infrastructure ever again.
