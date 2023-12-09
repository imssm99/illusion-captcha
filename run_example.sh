#!/bin/bash
uvicorn example:app --port=8000 &
pid1=$!
uvicorn api:app --port=8001 &
pid2=$!

trap "kill -TERM $pid1 $pid2" SIGINT
wait $pid1 $pid2