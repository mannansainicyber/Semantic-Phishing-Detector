import spacy

nlp = spacy.load("en_core_web_md")

PHISHING_PHRASES = [
    "confirm urgent account to release funds",
    "verify your password immediately",
    "your account has been suspended",
    "click here to avoid suspension",
    "congratulations you have won",
    "update billing information now",
    "unusual activity detected on your account",
    "your payment failed please update",
]

PHISHING_VECTORS = [nlp(p) for p in PHISHING_PHRASES]

def check_threat_level(text: str) -> float:
    token = nlp(text)
    return max(token.similarity(v) for v in PHISHING_VECTORS)

def get_ngrams(words, n):
    return [" ".join(words[i:i+n]) for i in range(len(words)-n+1)]

usr_input = input("Enter text to scan:\n>>> ")
words = usr_input.split()

# All the chunks we want to check
candidates = words + get_ngrams(words, 2) + get_ngrams(words, 3)

sentence_score = check_threat_level(usr_input)
max_score = max(check_threat_level(c) for c in candidates)

if sentence_score > 0.70 or max_score > 0.80:
    print(f"HIGH ALERT!!!!!! (Sentence: {sentence_score:.2f}, Max chunk: {max_score:.2f})")
elif sentence_score > 0.40:
    print("Mehhh, may be phishing but idk i dont get paid enough")
else:
    print("This is clear")
