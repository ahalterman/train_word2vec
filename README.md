train_word2vec
===============

Tools for training new word2vec models.

## Step 1: Prepare corpus

This code assumes that you're using a Wikipedia corpus. `wiki_prep.py` takes in
a Wikipedia dump and converts it into text file with one article per line. Example:

```
python wiki_prep.py arwiki-latest-pages-articles.xml.bz2 arabic_wiki.txt
```

## Step 2: Detect bigrams

word2vec works best when it knows to treat two word phrases as a single word
(e.g., "United_States", "political_science"). This function runs through the
text corpus (first argument) and applies gensim's bigram detector. It stores
the model with the name given in the second argument.

```
python detect_bigrams.py arabic_wiki.txt wiki_ar_bigram.model
```

## Step 3: Train model

`train_word2vec` takes in three arguments:

1. raw text file name
2. output file name
3. pre-built bigram model

```
python train_word2vec.py arabic_wiki.txt wiki_ar_word2vec.model wiki_ar_bigram.model
```

The parameters for word2vec are hardcoded into `train_word2vec.py`. Change them
in the source code.
