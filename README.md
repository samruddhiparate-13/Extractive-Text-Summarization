# Extractive Summarizaton
## Introduction

This is a simple extractive summarization algorithm based on the frequency of the words in the text. The algorithm is based on the idea that the more frequent a word is, the more important it is. The algorithm ranks sentences based on the frequency of the words that occur in them and then returns the top N sentences based on the rank.

## Usage

The algorithm is implemented in Python 3.6. or above The following packages are required before running the code:

* spaCy
    
    ```pip install -U pip setuptools wheel```

    ```pip install -U spacy```

    ``` pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.5.0/en_core_web_sm-3.5.0.tar.gz```

