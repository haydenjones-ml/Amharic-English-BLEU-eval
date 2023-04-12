import numpy
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

google_ref =  input('Input the "Google Translate" MT: ')
webtran_ref = input('Input the "webtran.eu" MT: ')
lingvanex_ref = input('Input the "Lingvanex" MT: ')
lesan_ref = input('Input the "Lesan.ai" MT: ')

hypo = input("Input the expected translation: ")

g_score = sentence_bleu([google_ref.split()], hypothesis=hypo.split(), weights=[1])
web_score = sentence_bleu([webtran_ref.split()], hypothesis=hypo.split(), weights=[1])
ling_score = sentence_bleu([lingvanex_ref.split()], hypothesis=hypo.split(), weights=[1])
l_score = sentence_bleu([lesan_ref.split()], hypothesis=hypo.split(), weights=[1])

print(f'\nGoogle Translate BLEU Score: {g_score}')
print(f'\nWebtran.eu BLEU Score: {web_score}')
print(f'\nLingvanex BLEU Score: {ling_score}')
print(f'\nLesan.ai BLEU Score: {l_score}')