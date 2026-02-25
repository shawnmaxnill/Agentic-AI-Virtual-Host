### (WIP) Agentic AI Host

This repo is in WIP state. Additions and improve pending are:

The aim of this project is to create an AI live host that ideally be hosted on social media sales platform aka Shopee/Tiktok Live.

This idea is to use RAG for product information and pass it to an LLM where it'll download a `.wav` file which would be played into a virtual model therefore 'speaking' to us.
This is reduce the workload of an actual person promoting the/a product.

We do not intend to replace human creative works with this, just to assist them in their downtime.

#### The repo consists of:

* An indexer directory called `pre_processing/` where documents and csv should be located to create a vecstore.
* `retrieval/` to fetch the data from vecstore and pass it to the LLM.
* `TTS_voice/` to generate a `.wav` file into `voicebank/` based on LLM output depending on which `voicebank/` voice used.
* `VTube_connection/` contains scripts for connecting to `VTube Studio` avaialable on `Steam`.
* `main.py` is the python script that merges everything together (Currently it just loads the vectors, runs the LLM and download a .wav file)


