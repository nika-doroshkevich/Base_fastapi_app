#!/bin/bash

alembic upgrade head

uvicorn main:main_app --host 0.0.0.0 --port 8000