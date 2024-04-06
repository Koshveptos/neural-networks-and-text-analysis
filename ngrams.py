from nltk.util import ngrams, bigrams

ste = list(bigrams(["я", "з", "ы", "к" ]))
pik = list(ngrams(["я", "з", "ы", "к" ], 3))  
print(ste)
print(pik)