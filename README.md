# Sentiment Analysis Tool for Armenian Books

This repository contains a Python-based tool for performing sentiment analysis on texts from the **Eastern Armenian National Corpus (EANC)**. The tool uses two popular sentiment analysis libraries — **VADER** and **TextBlob** — to analyze the sentiment of Armenian books. The goal is to provide insights into the sentiment trends and overall emotional tone of the literary works.

## Features

- **Sentiment Analysis**: Utilizes **VADER** and **TextBlob** to analyze sentiment on a sentence-by-sentence basis.
- **Eastern Armenian Support**: Specifically designed for analyzing books written in Eastern Armenian, using text from the **EANC**.

The script will generate a graph showing how sentiment changes across the text. The sentiment trend is visualized using polynomial interpolation, which smooths the sentiment scores over time for better clarity.
- X-axis: Represents the progression of the text (e.g. paragraphs).
- Y-axis: Represents sentiment polarity, ranging from negative to positive.

## Key Libraries Used

- **VADER Sentiment Analysis**: A lexicon and rule-based sentiment analysis tool for text data, well-suited for social media and informal texts.
- **TextBlob**: A simpler, more general-purpose NLP library that provides a range of text processing functions, including sentiment analysis.

## Installation

1. Install the dependencies:

```bash
pip install vaderSentiment textblob pandas scipy matplotlib beautifulsoup4 requests 
```

2. Clone the repository:

```bash
git clone https://github.com/Narekatsy/sentiment-analysis-armenian.git
cd sentiment-analysis-armenian
```