#!/bin/bash
# https://github.com/ggerganov/llama.cpp/discussions/2948

python llama.cpp/convert_hf_to_gguf.py ./models/Llama-3.2-3B-Instruct --outfile ./models/Llama-3.2-3B-Instruct.gguf --outtype q8_0