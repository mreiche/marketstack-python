#!/usr/bin/env bash

rm -rf openapi
openapi-python-client generate --path ../marketstack-openapi/marketstack-openapi.json --meta none
mv marketstack_open_api_client openapi
