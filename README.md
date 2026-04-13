# Semantic Phishing Detector

Hi, so this is a phishing detector I built basically instead of just looking for "bad words" like a basic filter it uses math to understand if someone is trying to scam you

I set a "target" sentence that sounds like a typical scam:

`confirm urgent account to release funds`

when you type something in, the AI converts your words into Embeddings (basically a giant map of numbers)

- if your sentence is "Please login to claim your money," the AI sees that "login" is close to "confirm" and "money" is close to "funds" on the map

- even though the words are different the math (Cosine Similarity) stays high

### How to set it up
1. clone this repo to your machine
2. install the requirements: 
   `pip install spacy scikit-learn`
3. download the AI model (the "map"):
   `python -m spacy download en_core_web_md`
4. run the script:
   `python main.py`

### Results I found
- **"immediate"** scored **0.74** because its semantically identical to "urgent."
- **"pizza"** scored **0.13** because the AI knows pizza isn't a threat (usually)
- **Full sentences** give higher scores because the AI understands the "vibe" of the whole message
