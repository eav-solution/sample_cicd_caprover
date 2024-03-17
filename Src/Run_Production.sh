#!/bin/bash

uvicorn main:app --host 0.0.0.0 --port 80 --timeout-keep-alive 600