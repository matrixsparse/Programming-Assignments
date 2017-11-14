#!/bin/sh
# @Copyright (C), 2017, matrix

case "$1" in
    start)
        /usr/local/mongodb/bin/mongod --maxConns 20000 --config /usr/local/mongodb/mongodb.conf
    ;;
    status)
        /usr/local/mongodb/bin/mongo localhost:27017/admin --eval "db.stats()"
    ;;
    stop)
        /usr/local/mongodb/bin/mongo localhost:27017/admin --eval "db.shutdownServer()"
    ;;
    restart)
        /usr/local/mongodb/bin/mongo localhost:27017/admin --eval "db.shutdownServer()"
        /usr/local/mongodb/bin/mongod --maxConns 20000 --config /usr/local/mongodb/mongodb.conf
    ;;
    *)
        echo "Usage: sh $(basename "$0") {start|status|stop|restart}"
        exit 1
esac
exit 0
