#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os.path
import sys
import multiprocessing
 
from gensim.corpora import  WikiCorpus
from gensim.models import Phrases
from gensim.models.word2vec import LineSentence
 
 
if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
 
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
 
    # check and process input arguments
 
    if len(sys.argv) < 3:
        print globals()['__doc__'] % locals()
        sys.exit(1)
    inp, outp = sys.argv[1:3]
 
    bigram = Phrases(LineSentence(inp))
 
    bigram.save(outp)
