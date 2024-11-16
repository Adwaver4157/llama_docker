#!/bin/bash

cd $(dirname $0)

IMAGE_NAME=weblab_llama:latest
CONTAINER_NAME="weblab_llama"

echo "$0: IMAGE=${IMAGE_NAME}"
echo "$0: CONTAINER=${CONTAINER_NAME}"

is_container_running() {
    RUNNING_CONTAINER_ID=$(docker ps -q -f name=${CONTAINER_NAME})
    if [ ! -z "${RUNNING_CONTAINER_ID}" ]; then
        docker container start ${CONTAINER_NAME}
        return 0
    else
        return 1
    fi
}

xhost +

docker run -it --rm \
    --privileged \
    --gpus all \
    --net host \
    --env DISPLAY=${DISPLAY} \
    --volume ${PWD}/:/root/workspace \
    --volume /dev/:/dev/ \
    --volume /tmp/.X11-unix:/tmp/.X11-unix \
    --name ${CONTAINER_NAME} \
    ${IMAGE_NAME} \
    bash -c "cd /root/workspace && bash"
