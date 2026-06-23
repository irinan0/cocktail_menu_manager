#!/bin/bash

# shellcheck disable=SC1072
if [ -f /tmp/dummy_data.json ]; then
cp / tmp / dummy_data.json / data / app_data.json
rm / tmp / dummy_data.json
fi

exec streamlit run / app / main.py - -server.port 80 - -server.address0.0.0.0