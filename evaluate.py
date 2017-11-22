# -*- coding: utf-8 -*-
from nltk.tag import CRFTagger
import re
import codecs
def get_data():
	with codecs.open('new-orchid97.pos', 'r',encoding='utf8') as f:
		lines = f.read()
	return re.split("TTTT",lines)
data=get_data()
i=0
data_all=[]
while i<len(data):
	data_list=[]
	for r in re.split('\n',data[i]):
		t=[x for x in re.split(' ',r) if x!='']
		if t!=[]:
			data_list.append((t[0],t[1]))
	data_all.append(data_list)
	i+=1
train_data=[x for x in data_all if x!=[]]
ct = CRFTagger()
ct.set_model_file('model.crf.tagger')
print(ct.evaluate(train_data))