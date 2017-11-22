# -*- coding: utf-8 -*-
from nltk.tag import CRFTagger
from pythainlp.tokenize import word_tokenize
ct = CRFTagger()
ct.set_model_file('model.crf.tagger')
text=""
while text!="exit":
	text=input("Text : ")
	post=word_tokenize(text,'icu')
	print(ct.tag_sents([post]))