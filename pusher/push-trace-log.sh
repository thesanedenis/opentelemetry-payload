#!/bin/bash
trace_id=$(openssl rand -hex 16)
span_id=$(openssl rand -hex 8)
timestamp=$(date +%s%N)

docker run --network host gardnera/tracepusher:v0.8.0  \
-ep http://127.0.0.1:4318 \
-sen Lenovo-DevOps \
-spn TestSpan \
-dur 12 \
--debug True \
--trace-id $trace_id \
--span-id $span_id


docker run --network host gardnera/logpusher:v0.1.0 \
  --endpoint http://127.0.0.1:4318 \
  --content "This is my log line from My Lenovov-DevOps host" \
  --debug True \
  --timestamp $timestamp \
  --trace-id $trace_id \
  --span-id $span_id 




