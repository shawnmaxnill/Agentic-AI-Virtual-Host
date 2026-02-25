# Run model and download wav
from retrieval.run_llm import create_chat_engine
from TTS_voice.python_default_TTS import speak


# Starting engine
chat = create_chat_engine()

print("LLM ready. Type 'exit' to stop.\n")

while True:
    query = input("You: ")

    if query.lower() in ["exit", "quit"]:
        break

    response = chat.ask(query)

    print("Bot:", response)

    wav_file = speak(response)
    print(f"\n{wav_file} generated")