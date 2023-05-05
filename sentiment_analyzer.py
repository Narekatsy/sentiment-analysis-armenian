from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import xml_parser as ps
from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

analyzer = SentimentIntensityAnalyzer()

# Apply sentiment analysis on translations column
def get_avg_sentiment(translations):
    scores = []
    
    for t in translations:
        # join all translations into a single string
        t_str = ", ".join(t)
        # compute sentiment score for the string
        score = analyzer.polarity_scores(t_str)
        scores.append(score["compound"])
        
    return scores

def split_and_analyze(df, num_splits = 20):
    # Combine all lists in dataframe into a single list of sentences
    all_sentences = [' '.join(row) for row in df]
    
    # Split the sentences into num_splits parts
    chunk_size = len(all_sentences) // num_splits
    sentence_chunks = [all_sentences[i:i+chunk_size] for i in range(0, len(all_sentences), chunk_size)]
    
    # Analyze the sentiment of each sentence chunk
    sentiment_scores = []
    for chunk in sentence_chunks:
        chunk_sentence = " ".join(chunk)
        sentiment_scores.append(analyzer.polarity_scores(chunk_sentence)['compound'])
        
    return sentiment_scores


if __name__ == "__main__":
    # The book file should be downloaded from EANC electornic library
    book_title = "Book_name.htm"
    
    # Creationg of a dataframe from a html file
    #df = ps.extract_words(book_title)
    
    # Creation of a dataframe from eanc.net library URL. Example below:
    df = ps.extract_words_web("http://eanc.net/EANC/library/Fiction/Original/Raffi/Short_Stories_8.htm?page=1&interface_language=en", 2)
    
    book_translation = df['translation']
    get_avg_sentiment(book_translation)

    scores = split_and_analyze(book_translation, 10)
    x = range(len(scores))
    
    f = interp1d(x, scores, kind='quadratic')

    # Create an array of points to evaluate the interpolator
    x_interp = np.linspace(0, len(scores) - 1, 100)
    
    # Evaluate the interpolator at the points
    y_interp = f(x_interp)
    
    plt.figure(figsize=(12, 8))
    plt.plot(x, scores, 'o', label='Sentiment Scores')
    plt.plot(x_interp, y_interp, label='Interpolated Curve')
    plt.xlabel('Part Number')
    plt.ylabel('Sentiment Score')
    plt.title("Հեղինակ - վերնագիր")
    plt.show()
    
