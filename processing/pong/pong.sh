#!/usr/bin/env bash

DATE=$(date -u +"%Y-%m-%dT%H:%M:%S.000Z")

echo "{\"msg\": \"pong\", \"process\": \"bash\", \"created\":\"${DATE}\"}"
