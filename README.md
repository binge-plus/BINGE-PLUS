# Prerequisites Setup Guide

This guide outlines the step-by-step process required to set up and configure the full Binge application infrastructure. Each step results in secrets or variables that are critical for the next step and must be added to your GitHub Actions secrets.

---

## 1. Clone and Set Up `binge-script` Repository

This repository contains the automation scripts necessary to set up and manage your infrastructure components.

**Steps:**

- Clone the repository:
  ```bash
  git clone https://github.com/your-org/binge-script.git
  cd binge-script
  ```

- Follow the instructions in the `README.md` of `binge-script` to:
  - Set up a **Google Cloud Platform (GCP) Service Account**
  - Generate and download the **GCP credentials JSON file**
  - Enable necessary APIs (Compute Engine, IAM, etc.)

**Output from this step:**
- `GCP_SERVICE_ACCOUNT_KEY` (add this to GitHub secrets)
- `GCP_PROJECT_ID`, `GCP_REGION`, and any relevant values

**Update GitHub Secrets:**
```
GCP_SERVICE_ACCOUNT_KEY=<Base64-encoded service account key>
GCP_PROJECT_ID=<your-project-id>
GCP_REGION=<your-region>
```

---

## 2. Configure `binge-infra` Repository

This repository manages your infrastructure as code (e.g., Terraform or Pulumi scripts).

**Steps:**

- Clone the repository:
  ```bash
  git clone https://github.com/your-org/binge-infra.git
  cd binge-infra
  ```

- Replace the default secrets and variables with the outputs from Step 1.
  - Update `terraform.tfvars` or environment-specific `.tfvars` files
  - Confirm correct bucket names, regions, and credentials

**Output from this step:**
- Infrastructure variables such as:
  - `TF_VAR_project_id`
  - `TF_VAR_region`
  - Any other GCP-related secrets used in infra provisioning

**Update GitHub Secrets:**
```
TF_VAR_project_id=<your-project-id>
TF_VAR_region=<your-region>
TF_VAR_credentials=<Base64-encoded GCP key if applicable>
```

---

## 3. Set Up `binge-ansible` Repository

This repo is used to configure all servers with required packages, security, and settings.

**Steps:**

- Clone the repository:
  ```bash
  git clone https://github.com/your-org/binge-ansible.git
  cd binge-ansible
  ```

- Update `group_vars` and secret files with the necessary credentials and environment settings.
- Modify roles to reflect services and configuration required by your application.
- Make sure Ansible can connect to your provisioned servers (SSH keys, inventory, etc.)

**Output from this step:**
- Server-specific credentials and keys
- Environment variable values for deployments
- SSH private key for accessing servers

**Update GitHub Secrets:**
```
ANSIBLE_SSH_PRIVATE_KEY=<your-private-key>
ANSIBLE_INVENTORY=<inventory-info>
APP_ENV_VARS=<Base64-encoded environment values>
```

---

## 4. Deploy Application via `binge-admin` Repository

This repo contains your application source code, organized by branches (dev, staging, prod).

**Steps:**

- Clone the repository:
  ```bash
  git clone https://github.com/your-org/binge-admin.git
  cd binge-admin
  ```

- Update the secrets and environment files according to your deployment environment.
- Set up CI/CD workflows to use the secrets you've stored.
- Configure the appropriate deployment branches.

**Output from this step:**
- Final application-specific secrets (e.g., API keys, DB URIs)
- Environment variable files for GitHub Actions

**Update GitHub Secrets:**
```
APP_SECRET_KEY=<your-app-secret>
DATABASE_URL=<your-db-uri>
EXTERNAL_API_KEYS=<your-api-keys>
```

---

## Final Note

Ensure that **every output from one step is securely stored as a GitHub Action Secret**, as it is required for the next step to function properly. This ensures a seamless, secure, and automated CI/CD pipeline across the entire Binge ecosystem.
