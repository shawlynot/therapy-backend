#!/usr/bin/env bash

set -e 
docker build -t ghcr.io/shawlynot/backend:latest .
docker push ghcr.io/shawlynot/backend:latest