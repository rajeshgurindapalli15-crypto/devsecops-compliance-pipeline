# DevSecOps Automated Compliance & Policy Enforcement Pipeline
![Build Status](https://github.com/rajeshgurindapalli15-crypto/devsecops-compliance-pipeline/actions/workflows/security-pipeline.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Security Guardrails](https://img.shields.io/badge/security-Bandit%20%7C%20pip--audit%20%7C%20Checkov-green)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue)
![License](https://img.shields.io/badge/license-MIT-green)

An enterprise-grade DevSecOps CI/CD security pipeline built with GitHub Actions. This repository demonstrates shifting security left by integrating static application security testing (SAST), software composition analysis (SCA), infrastructure-as-code (IaC) scanning, and custom automated policy gates into continuous deployment workflows.

---

## 🏗️ Architecture & Workflow Overview

## 🔐 Security Tooling Stack

| Domain | Tool | Description |
| :--- | :--- | :--- |
| **SAST** | [Bandit](https://github.com/PyCQA/bandit) | Analyzes Python source code for security flaws and common vulnerabilities. |
| **SCA** | [pip-audit](https://github.com/pypa/pip-audit) | Scans dependency manifests (`requirements.txt`) against known vulnerability databases (OSV/NVD). |
| **IaC Security** | [Checkov](https://www.checkov.io/) | Evaluates Terraform files (`main.tf`) for compliance and cloud security misconfigurations. |
| **Policy Engine** | `gatekeeper.py` | Custom Python policy gate that inspects project state and blocks non-compliant pipeline deployments. |

---

## 📂 Repository Structure

```text
.
├── .github/
│   └── workflows/
│       └── security-pipeline.yml  
├── app/
│   ├── main.py                     
│   └── requirements.txt           
├── infrastructure/
│   └── main.tf                     
└── security_policy/
    └── gatekeeper.py               
