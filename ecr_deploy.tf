provider "aws" {
    region = "us-west-2"
}

resource "random_string" "random_name" {
  length  = 10
  special = false
  upper   = false
}

resource "aws_ecr_repository" "newrepo" {
  name                 = "ase_repo-${random_string.random_name.result}"
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration {
    scan_on_push = true
  }
}
resource "null_resource" "run_script" {
depends_on = [
  aws_ecr_repository.newrepo
]
 provisioner "local-exec" {
    command = "/bin/bash script.sh"
  }
}

output "ecrreponame" {
  value = aws_ecr_repository.newrepo.name
}
output "ecrrepourl" {
   value = aws_ecr_repository.newrepo.repository_url
}

output "password" {
  value = "${data.aws_caller_identity.current.account_id}.dkr.ecr.us-west-2.amazonaws.com"
}
