# Setup
1. make .envrc and write hugging face token like the following
```
export HUGGINGFACE_TOKEN=your_token
```

2. make docker image
```
./BUILD-DOCKER-IMAGE.sh
```

3. run docker
```
./RUN-DOCKER-CONTAINER.sh
```