import sys
import os

def enforce_security_policy():
    print("[*] Running Automated DevSecOps Policy Gate...")
    
       
    policy_failed = False
    violations = [
        "[POLICY VIOLATION] Critical CVE found in dependency: Werkzeug==2.0.1",
        "[POLICY VIOLATION] IaC Misconfiguration: S3 Bucket 'my-extremely-insecure-audit-bucket-xyz' lacks public access block.",
        "[POLICY VIOLATION] IaC Security Group allows unrestricted ingress (0.0.0.0/0)."
    ]
    
    print("\n--- Security Scan Audit Summary ---")
    for v in violations:
        print(v)
    
   
    if len(violations) > 0:
        print("\n[!] GATE FAILURE: Security threshold breached. Blocking deployment to production.")
        sys.exit(1)
    else:
        print("\n[+] GATE PASSED: All security checks cleared successfully.")
        sys.exit(0)

if __name__ == "__main__":
    enforce_security_policy()