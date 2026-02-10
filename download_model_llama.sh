mkdir -p ~/models
cd ~/models

# Model download URL
URL="https://huggingface.co/RichardErkhov/meta-llama_-_Llama-2-7b-chat-hf-gguf/resolve/main/Llama-2-7b-chat-hf.Q4_K_M.gguf"

# Output filename
OUTPUT="Llama-2-7b-chat-hf.Q4_K_M.gguf"

echo "Downloading model..."
wget -c "$URL" -O "$OUTPUT"

echo "Download complete."
