#!/bin/bash
 
USER=$1

(curl -f -s \
     -H "Content-type:application/json" \
     -H "X-Auth-Token:YOUR_AUTH_TOKEN" \
     -H "X-User-Id:YOUR_USER_ID" \
     -X POST \
     https://techflow.cloud/api/v1/users.delete \
     -d '{"username": "'$USER'"}' \
     && \
     echo -e "\n $USER removed") \
     || { echo "Request failed, performing action..."; exit 1; }
