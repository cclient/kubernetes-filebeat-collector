#!/bin/sh
if [ $state != "ok" ]
then
    redis-cli -h $host -p $port -n $db set $contain 1
else
    redis-cli -h $host -p $port -n $db del $contain
fi
