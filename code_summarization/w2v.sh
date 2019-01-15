#!/bin/sh

W2VDIR=/work/pauldhein/trunk/
IN=./data/corpus/comm-sentences.output

time $W2VDIR/word2vec -train $IN -output comm-vectors.txt -cbow 0 -size 50 -window 5 -negative 0 -hs 1 -sample 1e-3 -threads 12 -binary 0

# $W2VDIR/distance vectors.txt.bin
