#!/bin/bash

# run with docker
docker run -d --name tmway -v $PWD/inventory:/inventory -e HTTP_PORT=8081 -p 8081:8081 miladpav/inventory_generator:1.0