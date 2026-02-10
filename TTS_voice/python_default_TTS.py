import subprocess
import uuid
import os

# Voice model
MODEL = os.path.join(os.path.dirname(__file__), "../voicebank/piper/en_US-lessac-medium.onnx")

def speak(text, out_dir = os.path.join(os.path.dirname(__file__),"../voicebank/voice_db")):
    import os
    os.makedirs(out_dir, exist_ok=True)

    out_file = f"{out_dir}/{uuid.uuid4().hex}.wav"

    subprocess.run(
        [
            "piper",
            "--model", MODEL,
            "--output_file", out_file
        ],
        input=text.encode("utf-8"),
        check=True
    )

    return out_file