#!/bin/bash
huggingface-cli login --token $HUGGINGFACE_TOKEN
huggingface-cli download meta-llama/Llama-3.2-3B-Instruct --local-dir models/Llama-3.2-3B-Instruct
