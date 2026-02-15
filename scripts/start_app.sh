#!/bin/bash

# Fail only if a command truly fails
set -e

echo "Reloading systemd"
systemctl daemon-reload

echo "Restarting python-app service"
systemctl restart python-app

echo "Waiting for service to stabilize"
sleep 3

echo "Checking service status"
systemctl is-active --quiet python-app

echo "Service is running"
exit 0
