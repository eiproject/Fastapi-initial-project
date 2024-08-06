docker build -f DockerFile -t startship:$1 .
docker tag startship:$1 startship:latest