#!/bin/bash

if [[ "$TRAVIS_BRANCH" = "master" ]] && [[ "$TRAVIS_PULL_REQUEST" = "false" ]]; then
    echo -e "\033[00;32m========================================================";
    echo -e "Redeploying ECS Task...";
    echo -e "========================================================\033[0m";

    aws ecs update-service --cluster ${ECS_CLUSTER} --region ${ECS_REGION} --service ${ECS_SERVICE} --force-new-deployment

    echo -e "\033[00;32m========================D=O=N=E=========================\033[0m\n";
fi;