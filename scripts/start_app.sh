#!/bin/bash
set -e

systemctl daemon-reload
systemctl start python-app

sleep 5
systemctl is-active --quiet python-app
