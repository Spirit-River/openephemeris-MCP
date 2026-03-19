#!/bin/bash

# OpenEphemeris Human Design Transit Generator
# Calculates the live activation matrix for any individual

# Requires OPENEPHEMERIS_API_KEY environment variable
if [ -z "$OPENEPHEMERIS_API_KEY" ]; then
    echo "Please set OPENEPHEMERIS_API_KEY"
    exit 1
fi

curl -X POST "https://api.openephemeris.com/human-design/composite" \
  -H "Authorization: Bearer $OPENEPHEMERIS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "person_1": {
      "datetime": "1995-10-18T05:00:00Z",
      "longitude": -0.1276,
      "latitude": 51.5072
    },
    "person_2": {
      "datetime": "2026-06-25T12:00:00Z",
      "longitude": -0.1276,
      "latitude": 51.5072
    },
    "composite_type": "transit"
  }'

echo -e "\n\nThis generates the full composite bodygraph with both defined and open centers according to Ra Uru Hu's mechanics."
