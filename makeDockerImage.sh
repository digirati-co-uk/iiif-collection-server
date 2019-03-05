#!/bin/bash

echo -e "\033[00;32m========================================================";
echo -e "Building Docker image...";
echo -e "========================================================\033[0m";

docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
docker build --file=./Dockerfile \
    -t iiif-collection-server:latest \
    .

if [[ "$(docker images -q iiif-collection-server:latest 2> /dev/null)" == "" ]]; then
  echo -e "\033[00;32m ===> Image was NOT built, failing the build";
  exit 1
fi

if [[ "$TRAVIS_BRANCH" = "master" ]] && [[ "$TRAVIS_PULL_REQUEST" = "false" ]]; then
  echo -e "\033[00;32m ===> Pushing to Dockerhub\033[0m\n";
  docker tag iiif-collection-server:latest digirati/iiif-collection-server:latest
  docker push digirati/iiif-collection-server:latest
else
    echo -e "\033[00;31m ===> Skipping push to Dockerhub\033[0m\n";
fi;
echo -e "\033[00;32m====================S=U=C=C=E=S=S=======================\033[0m\n";
