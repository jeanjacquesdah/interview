# Specify the AWS provider and region with variables
provider "aws" {
  region = var.aws_region
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}

# Create a VPC
resource "aws_vpc" "my_vpc" {
  cidr_block = var.vpc_cidr_block
  enable_dns_support = true
  enable_dns_hostnames = true
  tags = {
    Name = "MyVPC"
  }
}

# Create a subnet within the VPC
resource "aws_subnet" "my_subnet" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = var.subnet_cidr_block
  availability_zone       = var.subnet_availability_zone
  map_public_ip_on_launch = true
  tags = {
    Name = "MySubnet"
  }
}

# Create a security group allowing inbound traffic on port 80
resource "aws_security_group" "my_security_group" {
  vpc_id = aws_vpc.my_vpc.id

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "MySecurityGroup"
  }
}

# Create an EC2 instance in the subnet with user data for installing a web server
resource "aws_instance" "my_instance" {
  ami             = var.instance_ami
  instance_type   = var.instance_type
  key_name        = var.key_pair_name
  subnet_id       = aws_subnet.my_subnet.id
  security_group  = [aws_security_group.my_security_group.id]
  associate_public_ip_address = true

  user_data = <<-EOF
              #!/bin/bash
              apt-get update
              apt-get install -y apache2
              systemctl enable apache2
              systemctl start apache2
              EOF

  tags = {
    Name = "MyInstance"
  }
}

