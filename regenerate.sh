#!/usr/bin/env bash

openapi-python-client update --path ../marketstack-openapi/marketstack-openapi.json --meta none --config generator-config.yml
PYTHONPATH="." pytest tests/test_models.py
