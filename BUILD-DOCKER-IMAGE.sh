#!/bin/bash

docker build . -f docker/Dockerfile -t weblab_uv:latest
docker build . -f docker/Dockerfile.llama -t weblab_llama:latest
