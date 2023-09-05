#!/bin/bash

USER=$1
EMAIL=$USER@mail
PASS=$(openssl rand -base64 12)


(curl -f -s \
     -H "Content-type:application/json" \
     -H "X-Auth-Token:YOUR_AUTH_TOKEN" \
     -H "X-User-Id:YOUR_USER_ID" \
     https://your-rocket-chat-server/api/v1/users.create \
     -d '{"name":"'$USER'","email":"'$EMAIL'","password":"'$PASS'","username":"'$USER'","verified":true}' > /dev/null \
&& \
echo "$USER    $PASS  $(date)") >> users.txt\
|| { echo "Request failed, performing action..."; exit 1; }

echo -e '\n \n'
tail -1 users.txt
echo -e '\n \n'
