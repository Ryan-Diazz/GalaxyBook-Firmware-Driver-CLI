#!/usr/bin/env bash

echo "Cleaning Python build artifacts..."

find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f \( -name "*.pyc" -o -name "*.pyo" \) -delete
find . -type d -name ".pytest_cache" -exec rm -rf {} +
find . -type d -name ".mypy_cache" -exec rm -rf {} +
find . -type d -name "*.debhelper" -exec rm -rf {} +
find . -type d -name ".pybuild" -exec rm -rf {} +
find . -type d -name ".build-venv" -exec rm -rf {} +
find . -type d -name "build" -exec rm -rf {} +
find . -type d -name "dist" -exec rm -rf {} +
find . -type d -name "deb_dist" -exec rm -rf {} +
find . -type d -name "*.egg-info" -exec rm -rf {} +

echo "Done."