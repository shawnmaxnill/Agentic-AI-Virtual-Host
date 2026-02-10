#!/usr/bin/env bash

set -e

MODEL_DIR="$HOME/piper/models"

echo "Creating model directory at $MODEL_DIR..."
mkdir -p "$MODEL_DIR"
cd "$MODEL_DIR"

# Voice selection: English US Lessac medium
echo "Downloading en_US-lessac-medium model and config..."

wget -O en_US-lessac-medium.onnx \
    "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/lessac/medium/en_US-lessac-medium.onnx?download=true"

wget -O en_US-lessac-medium.onnx.json \
    "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/lessac/medium/en_US-lessac-medium.onnx.json?download=true"

echo "Downloads completed in $MODEL_DIR"
echo "Model: en_US-lessac-medium.onnx"
echo "Config: en_US-lessac-medium.onnx.json"

