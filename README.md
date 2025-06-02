# Prerequisites Setup Guide

This guide outlines the sequential setup of all repositories involved in the Binge application infrastructure. Each step will generate secrets and configurations that must be saved and passed to the **next repository's GitHub Secrets** for successful CI/CD and deployment automation.

---

## 1. Clone and Set Up `binge-script` Repository

This repository contains automation scripts to initialize foundational services like GCP access and required APIs.

**Steps:**

- Clone the repository:
  ```bash
  git clone https://github.com/your-org/binge-script.git
  cd binge-script
  ```

- Follow the instructions in `README.md` to:
  - Set up a **GCP Service Account**
  - Generate the **GCP credentials JSON file**
  - Enable required APIs (Compute, IAM, Storage, etc.)

**Secrets Generated (for the *next repo* `binge-infra`):**
```
GCP_SERVICE_ACCOUNT_KEY=<Base64-encoded JSON>
GCP_PROJECT_ID=<your-project-id>
GCP_REGION=<your-region>
```

👉 **Save these in the `binge-infra` repository GitHub Secrets.**

---

## 2. Configure `binge-infra` Repository

This repository manages cloud infrastructure using tools like Terraform or Pulumi.

**Steps:**

- Clone the repository:
  ```bash
  git clone https://github.com/your-org/binge-infra.git
  cd binge-infra
  ```

- Update your `.tfvars` or environment files using the secrets from `binge-script`.

- Provision your infrastructure (VMs, buckets, networks, etc.)

**Secrets Generated (for the *next repo* `binge-ansible`):**
```
INFRA_SSH_PRIVATE_KEY=<SSH key to access servers>
INFRA_VM_IPS=<Comma-separated list of provisioned VM IPs>
GCP_PROJECT_ID=<Used again for context>
```

👉 **Save these in the `binge-ansible` repository GitHub Secrets.**

---

## 3. Set Up `binge-ansible` Repository

This repository configures all provisioned servers with necessary packages, users, and services.

**Steps:**

- Clone the repository:
  ```bash
  git clone https://github.com/your-org/binge-ansible.git
  cd binge-ansible
  ```

- Configure `group_vars` and roles as needed.
- Use the secrets from `binge-infra` for Ansible SSH access and VM targeting.

**Secrets Generated (for the *next repo* `binge-admin`):**
```
DEPLOYMENT_SSH_KEY=<Private key used for deployments>
DEPLOYMENT_HOSTS=<List of application server IPs>
APP_ENV_VARS=<Base64-encoded .env file contents>
```

👉 **Save these in the `binge-admin` repository GitHub Secrets.**

---

## 4. Deploy Application via `binge-admin` Repository

This repository contains your actual application code and GitHub Actions for deployment.

**Steps:**

- Clone the repository:
  ```bash
  git clone https://github.com/your-org/binge-admin.git
  cd binge-admin
  ```

- Configure your GitHub Actions workflows to use secrets from `binge-ansible`.

- Set up environment-specific branches (e.g., `dev`, `staging`, `prod`).

**Secrets Used (from previous step):**
```
DEPLOYMENT_SSH_KEY
DEPLOYMENT_HOSTS
APP_ENV_VARS
```

---

## Final Note

➡️ **Every repository's setup outputs secrets that must be saved in the *next repository’s* GitHub Secrets**. This ensures that the GitHub Actions pipelines in each stage have the necessary credentials and context to proceed.

Always **encrypt sensitive values** before storing and **double-check repository access permissions**.
