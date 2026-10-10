provider "aws" {
  region = "us-east-1"
}

# INTENTIONAL VULNERABILITY: S3 bucket without public access block and encryption
resource "aws_s3_bucket" "insecure_bucket" {
  bucket = "my-extremely-insecure-audit-bucket-xyz"
}

resource "aws_s3_bucket_acl" "example" {
  bucket = aws_s3_bucket.insecure_bucket.id
  acl    = "public-read"
}

# INTENTIONAL VULNERABILITY: Security group allowing inbound traffic from anywhere on all ports
resource "aws_security_group" "allow_all" {
  name        = "allow_all_sg"
  description = "Allow all inbound traffic"

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}