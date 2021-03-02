#!/usr/bin/python3
# -*- coding: utf-8 -*-
import docker

try:
    client = docker.from_env()
except docker.errors.DockerException:
    pass
# client.containers.run("ubuntu", "echo hello world")
# client.containers.run("bfirsh/reticulate-splines", detach=True)
containers = client.containers.list()
# container = client.containers.get('4536d2de7c54')
print('client:', client)
print('containers:', containers)
container_id = containers[0].id
print(container_id, type(container_id))
container = client.containers.get(container_id)
print(container)
