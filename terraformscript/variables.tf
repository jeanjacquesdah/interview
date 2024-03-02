variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "aws_access_key" {
  description = "AWS access key"
}

variable "aws_secret_key" {
  description = "AWS secret key"
}

variable "vpc_cidr_block" {
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
}

variable "subnet_cidr_block" {
  description = "CIDR block for the subnet"
  default     = "10.0.1.0/24"
}

variable "subnet_availability_zone" {
  description = "Availability zone for the subnet"
  default     = "us-east-1a" # choose the availability zone of your choice 
}

variable "instance_ami" {
  description = "AMI ID for the EC2 instance"
  default     = "ami-0c55b159cbfaze1f0" # choose the AMI of your choice this is just an example 
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "key_pair_name" {
  description = "Name of the key pair for the EC2 instance"
}

