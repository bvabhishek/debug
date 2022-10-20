provider "aws" {
    region = "us-west-2"
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
