#!/bin/bash
# download_gpt4all_j.sh

# Create a folder for models
mkdir -p ~/models
cd ~/models

# Download the GPT4All-J model
MODEL_URL="https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin"
wget $MODEL_URL -O ggml-gpt4all-j.bin

# Optional: test if it exists
if [ -f "ggml-gpt4all-j.bin" ]; then
    echo "Model downloaded successfully!"
else
    echo "Download failed!"
fi
