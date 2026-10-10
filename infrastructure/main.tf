provider "aws" {
  region = "us-east-1"
}

# SECURED: S3 bucket with restricted access
resource "aws_s3_bucket" "secure_bucket" {
  bucket = "my-secure-audit-bucket-xyz"
}

resource "aws_s3_bucket_public_access_block" "secure_bucket_block" {
  bucket                  = aws_s3_bucket.secure_bucket.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# SECURED: Security group restricting inbound traffic to internal network
resource "aws_security_group" "allow_restricted" {
  name        = "allow_restricted_sg"
  description = "Allow restricted inbound traffic"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/16"]
  }
}