#!/bin/bash
aws cloudformation deploy \
    --template-file template.yaml \
    --stack-name SelfStorageBackend \
    --capabilities CAPABILITY_NAMED_IAM
