terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "ap-south-1"
}

variable "key_name" {
  type        = string
  description = "Existing EC2 key pair in Mumbai"
}

variable "my_ip" {
  type        = string
  description = "Your public IPv4 address"
}

data "aws_ami" "windows" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["Windows_Server-2022-English-Full-Base-*"]
  }

  filter {
    name   = "architecture"
    values = ["x86_64"]
  }
}

resource "aws_security_group" "windows_sg" {
  name        = "terraform-windows-rdp"
  description = "Allow RDP from my IP"

  ingress {
    from_port   = 3389
    to_port     = 3389
    protocol    = "tcp"
    cidr_blocks = ["${var.my_ip}/32"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Terraform-Windows-SG"
  }
}

resource "aws_instance" "windows_vm" {
  ami                    = data.aws_ami.windows.id
  instance_type          = "t3.micro"
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.windows_sg.id]

  root_block_device {
    volume_size = 30
    volume_type = "gp3"
  }

  tags = {
    Name = "Terraform-Windows-VM"
  }
}

output "instance_id" {
  value = aws_instance.windows_vm.id
}

output "public_ip" {
  value = aws_instance.windows_vm.public_ip
}
