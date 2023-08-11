#!/usr/bin/env bash
set -e
BUILD_NUMBER=${1:-latest}
APPS_DIRS=(
  client
  server
  )
CR_REPO=${2:-thesanedenis}
IMAGES=""

docker --version

for dir in "${APPS_DIRS[@]}"
  do
    image_tag=${CR_REPO}/${dir}:${BUILD_NUMBER}
    docker build -t $image_tag ./${dir}
    docker push $image_tag
    echo "Image -> $image_tag was pushed to repository -> $CR_REPO"
  done
