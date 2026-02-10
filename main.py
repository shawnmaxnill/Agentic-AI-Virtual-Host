from retrieval.run_llm import answer_query
from TTS_voice.python_default_TTS import speak


# Inserting prompt
LLM_response = answer_query("Im looking to make a smoothie, any recommendations?")
print(LLM_response)

# Creating wav file
wav_file = speak(LLM_response)
print(f"/n{wav_file} generated")
