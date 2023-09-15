#!/bin/bash
set -e

port=${PORT:-5000}
gunicorn app:app --bind 0.0.0.0:$port