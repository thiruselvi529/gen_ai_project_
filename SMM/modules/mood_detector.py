from textblob import TextBlob

def detect_mood(text):

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if "travel" in text.lower():
        return "travel"

    elif polarity > 0.3:
        return "happy"

    elif polarity < -0.3:
        return "sad"

    else:
        return "motivational"