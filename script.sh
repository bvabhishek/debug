#!/usr/bin/env bash
aws ecr get-login-password --region us-west-2 | docker login  --username AWS  --password-stdin $(terraform output --raw password)
docker build -t $(terraform output --raw ecrreponame) Dockerfile .
docker tag $(terraform output --raw ecrreponame):latest $(terraform output --raw ecrrepourl):latest
docker push $(terraform output --raw ecrrepourl):latest
