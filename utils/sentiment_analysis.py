import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the VADER lexicon if it's not already present
nltk.download('vader_lexicon', quiet=True)

class SentimentAnalyzer:
    def __init__(self):
        """
        Initializes the SentimentIntensityAnalyzer from NLTK.
        """
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        """
        Analyzes the sentiment of a given text.

        :param text: The text to analyze.
        :return: A dictionary containing the scores for each sentiment.
        """
        return self.analyzer.polarity_scores(text)
    
    
