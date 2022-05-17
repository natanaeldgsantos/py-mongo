#!/bin/bash

conda create -n mongo python:3.9

conda activate mongo

python -m pip install pymongo dnspython python-dotenv pandas Faker