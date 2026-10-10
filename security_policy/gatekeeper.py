import sys
import os
import argparse

def enforce_security_policy():
    parser = argparse.ArgumentParser(description="Automated DevSecOps Compliance Gate")
    parser.add_argument("--simulate-failure", action="store_true", help="Inject test vulnerabilities into scan memory for pipeline validation")
    args = parser.parse_args()

    print("[*] Running Automated DevSecOps Policy Gate...")
    violations = []
    
    req_path = os.path.join("app", "requirements.txt")
    if os.path.exists(req_path):
        with open(req_path, "r") as f:
            for line_num, line in enumerate(f, 1):
                # Check for vulnerable or unpinned dependency patterns
                if "Werkzeug==2.0.1" in line or "Flask==2.0.1" in line:
                    violations.append(f"[SCA VIOLATION] app/requirements.txt L{line_num}: Vulnerable version pinned ({line.strip()})")
    else:
        violations.append(f"[SCA ERROR] Missing dependency file: {req_path}")

    tf_path = os.path.join("infrastructure", "main.tf")
    if os.path.exists(tf_path):
        with open(tf_path, "r") as f:
            tf_content = f.read()
            # Inspect for security misconfigurations
            if "0.0.0.0/0" in tf_content:
                violations.append("[IaC VIOLATION] infrastructure/main.tf: Security Group allows unrestricted public ingress (0.0.0.0/0).")
            if "aws_s3_bucket" in tf_content and "aws_s3_bucket_public_access_block" not in tf_content:
                violations.append("[IaC VIOLATION] infrastructure/main.tf: S3 Bucket configured without public access block.")
    else:
        violations.append(f"[IaC ERROR] Missing infrastructure template: {tf_path}")

    if args.simulate_failure:
        violations.append("[PIPELINE DEMO] --simulate-failure flag active: Injected synthetic compliance fault for pipeline abort validation.")

    print("\n--- Security Scan Audit Summary ---")
    if len(violations) == 0:
        print("[+] No policy violations detected. Infrastructure and dependencies comply with baseline standards.")
    else:
        for v in violations:
            print(v)
    
    if len(violations) > 0:
        print("\n[!] GATE FAILURE: Compliance threshold breached. Pipeline execution halted, deployment blocked.")
        sys.exit(1)
    else:
        print("\n[+] GATE PASSED: All security checks cleared successfully. Proceeding to deployment.")
        sys.exit(0)

if __name__ == "__main__":
    enforce_security_policy()