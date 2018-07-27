#!/bin/sh
redis-cli -h $host -p $port -n $db exists $contain