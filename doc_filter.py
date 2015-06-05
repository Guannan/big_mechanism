#!/usr/bin/env python

import sys
import collections
import operator
import random
import math
import numpy as np
from sklearn import svm

def _complete():
	"""
	Finds where a title or abstract text
	ends and outputs the entire string
	"""
	output = ''
	for line in sys.stdin:
		if '  - ' not in line and ' - ' not in line:
			output += ' ' + line.strip()
		else:
			return output
	return output

def _clean_text(word):
	"""
	Removes punctuation information
	"""
	global stop_words
	global stem_patterns
	chars_to_remove = ['.', ',', '?', '!', '*', '(', ')']
	word = word.translate(None, ''.join(chars_to_remove))
	word = word.lower()
	if word in stop_words:
		return None
	if 'http' in word:
		return None
	for stem_pattern in stem_patterns:
		if word.endswith(stem_pattern):
			word = word[:-len(stem_pattern)]
			break
	return word

def _parse_unigram(text_list):
	"""
	Returns a dictionary of unigrams
	with the keys being the words and 
	the columns being the occurrences
	"""
	unigrams = collections.defaultdict(int)
	doc_occurrence = collections.defaultdict(int)  # number of docs word occurs in
	tf = collections.defaultdict(float)   # weighted frequency of word occurrence in 1 doc
	total_doc_count = len(text_list)

	counted = False
	occurrence = collections.defaultdict(int)
	for text in text_list:
		words = text.strip().split(' ')
		for i in xrange(len(words)):
			word = words[i]
			temp = _clean_text(word)  # TODO optimize
			if temp != None:
				word = temp
				unigrams[word] += 1
				occurrence[word] += 1
				if not counted:
					doc_occurrence[word] += 1
					counted = True
		for word, count in occurrence.iteritems():
			tf[word] += float(count)/total_doc_count
		occurrence = collections.defaultdict(int)
		counted = False

	idf = collections.defaultdict(float)
	for word, doc_count in doc_occurrence.iteritems():
		idf[word] = math.log(float(total_doc_count)/doc_count)
	
	tf_idf = collections.defaultdict(float)
	for word in idf:
		tf_idf[word] += tf[word] * idf[word]
	return unigrams, tf_idf

def _parse_bigram(text_list):
	"""
	Returns a dictionary of bigrams
	with the keys being the words and 
	the columns being the occurrences
	"""
	bigrams = collections.defaultdict(int)
	doc_occurrence = collections.defaultdict(int)  # number of docs word occurs in
	tf = collections.defaultdict(float)   # weighted frequency of word occurrence in 1 doc
	total_doc_count = len(text_list)

	counted = False
	occurrence = collections.defaultdict(int)
	for text in text_list:
		words = text.strip().split(' ')
		for i in xrange(len(words)-1):
			word_one = words[i]
			word_one = _clean_text(word_one)
			word_two = words[i + 1]
			word_two = _clean_text(word_two)
			if word_one != None and word_two != None:
				bigram = ' '.join([word_one, word_two])
				bigrams[bigram] += 1
				occurrence[bigram] += 1
				if not counted:
					doc_occurrence[bigram] += 1
					counted = True
		for word, count in occurrence.iteritems():
			tf[word] += float(count)/total_doc_count
		occurrence = collections.defaultdict(int)
		counted = False

	idf = collections.defaultdict(float)
	for word, doc_count in doc_occurrence.iteritems():
		idf[word] = math.log(float(total_doc_count)/doc_count)
	
	tf_idf = collections.defaultdict(float)
	for word in idf:
		tf_idf[word] += tf[word] * idf[word]		

	return bigrams, tf_idf

def _parse_trigram(text_list):
	"""
	Returns a dictionary of trigrams
	with the keys being the words and 
	the columns being the occurrences
	"""
	trigrams = collections.defaultdict(int)

	for text in text_list:
		words = text.strip().split(' ')
		for i in xrange(len(words)-2):
			word_one = words[i]
			word_one = _clean_text(word_one)
			word_two = words[i + 1]
			word_two = _clean_text(word_two)
			word_three = words[i + 2]
			word_three = _clean_text(word_three)
			if word_one != None and word_two != None and word_three != None:
				trigram = ' '.join([word_one, word_two, word_three])
				trigrams[trigram] += 1

	return trigrams

def _generate_ngrams():
	global good_count
	global bad_count
	global title_list_good
	global title_list_bad
	global abstract_list_good
	global abstract_list_bad

	unigrams = _parse_unigram(title_list_good)
	sorted_unigrams = sorted(unigrams.items(), key=operator.itemgetter(1))
	fh = open('good_unigram_title.txt', 'w')
	for word, count in reversed(sorted_unigrams):
		fh.write(word + ' ' + str(float(count)/good_count) + '\n')

	unigrams = _parse_unigram(title_list_bad)
	sorted_unigrams = sorted(unigrams.items(), key=operator.itemgetter(1))
	fh = open('bad_unigram_title.txt', 'w')
	for word, count in reversed(sorted_unigrams):
		fh.write(word + ' ' + str(float(count)/bad_count) + '\n')

	unigrams = _parse_unigram(abstract_list_good)
	sorted_unigrams = sorted(unigrams.items(), key=operator.itemgetter(1))
	fh = open('good_unigram_abstract.txt', 'w')
	for word, count in reversed(sorted_unigrams):
		fh.write(word + ' ' + str(float(count)/good_count) + '\n')

	unigrams = _parse_unigram(abstract_list_bad)
	sorted_unigrams = sorted(unigrams.items(), key=operator.itemgetter(1))
	fh = open('bad_unigram_abstract.txt', 'w')
	for word, count in reversed(sorted_unigrams):
		fh.write(word + ' ' + str(float(count)/bad_count) + '\n')

	bigrams = _parse_bigram(title_list_good)
	sorted_bigrams = sorted(bigrams.items(), key=operator.itemgetter(1))
	fh = open('good_bigram_title.txt', 'w')
	for word, count in reversed(sorted_bigrams):
		fh.write(word + ' ' + str(float(count)/good_count) + '\n')

	bigrams = _parse_bigram(title_list_bad)
	sorted_bigrams = sorted(bigrams.items(), key=operator.itemgetter(1))
	fh = open('bad_bigram_title.txt', 'w')
	for word, count in reversed(sorted_bigrams):
		fh.write(word + ' ' + str(float(count)/bad_count) + '\n')

	bigrams = _parse_bigram(abstract_list_good)
	sorted_bigrams = sorted(bigrams.items(), key=operator.itemgetter(1))
	fh = open('good_bigram_abstract.txt', 'w')
	for word, count in reversed(sorted_bigrams):
		fh.write(word + ' ' + str(float(count)/good_count) + '\n')

	bigrams = _parse_bigram(abstract_list_bad)
	sorted_bigrams = sorted(bigrams.items(), key=operator.itemgetter(1))
	fh = open('bad_bigram_abstract.txt', 'w')
	for word, count in reversed(sorted_bigrams):
		fh.write(word + ' ' + str(float(count)/bad_count) + '\n')

	trigrams = _parse_trigram(title_list_good)
	sorted_trigrams = sorted(trigrams.items(), key=operator.itemgetter(1))
	fh = open('good_trigram_title.txt', 'w')
	for word, count in reversed(sorted_trigrams):
		fh.write(word + ' ' + str(float(count)/good_count) + '\n')

	trigrams = _parse_trigram(title_list_bad)
	sorted_trigrams = sorted(trigrams.items(), key=operator.itemgetter(1))
	fh = open('bad_trigram_title.txt', 'w')
	for word, count in reversed(sorted_trigrams):
		fh.write(word + ' ' + str(float(count)/bad_count) + '\n')

	trigrams = _parse_trigram(abstract_list_good)
	sorted_trigrams = sorted(trigrams.items(), key=operator.itemgetter(1))
	fh = open('good_trigram_abstract.txt', 'w')
	for word, count in reversed(sorted_trigrams):
		fh.write(word + ' ' + str(float(count)/good_count) + '\n')

	trigrams = _parse_trigram(abstract_list_bad)
	sorted_trigrams = sorted(trigrams.items(), key=operator.itemgetter(1))
	fh = open('bad_trigram_abstract.txt', 'w')
	for word, count in reversed(sorted_trigrams):
		fh.write(word + ' ' + str(float(count)/bad_count) + '\n')

def _get_tableless_id():
	global tableless_id

	tableless_id = []
	for line in open("no_table_papers.txt", 'r'):
		tableless_id.append(line.strip())

def _parse_labeled_data():
	global labeled_data
	global training_data_label
	global test_data_label
	global tableless_id

	_get_tableless_id()
	random.seed()
	labeled_data = collections.defaultdict(str)
	training_data_label = collections.defaultdict(str)
	test_data_label = collections.defaultdict(str)

	for line in open("labeled_preprocessing_data.txt", 'r'):
		temp = line.strip().split(',')
		if not temp[0] in tableless_id:
			labeled_data[temp[0]] = temp[1]  # match pmc id with labels Y, ?, N
			num = random.randint(0,9)
			if num >= 8:  # ratio of training vs test data
				test_data_label[temp[0]] = temp[1]
			else:
				training_data_label[temp[0]] = temp[1]

def _svm_train():
	global papers
	global training_data_label
	global feature_list

	feature_count = 50
	word_occurrence = collections.defaultdict(int)
	log_likelihood = collections.defaultdict(float)
	training_data = np.zeros((len(training_data_label), feature_count))
	training_target = np.zeros((len(training_data_label)))

	tf_idf = collections.defaultdict(float)
	for pmcid, values in papers.iteritems():
		id_num = pmcid[3:]  # remove 'PMC' tag
		if training_data_label[id_num]:
			bigrams, scores = _parse_bigram([values['title']])
			for word, score in scores.iteritems():
				tf_idf[word] += score
			bigrams, scores = _parse_bigram([values['abstract']])
			for word, score in scores.iteritems():
				tf_idf[word] += score

	cur_feature_num = 0
	feature_list = []
	feature_vec = []

	sorted_tf_idf = sorted(tf_idf.items(), key=operator.itemgetter(1))
	for word, count in reversed(sorted_tf_idf):
		cur_feature_num += 1
		feature_list.append(word)
		if cur_feature_num >= feature_count:
			break

	example_count = 0
	for pmcid, values in papers.iteritems():
		id_num = pmcid[3:]  # remove 'PMC' tag
		if training_data_label[id_num]:
			bigrams, junk = _parse_bigram([values['title']])
			for word, count in bigrams.iteritems():
				word_occurrence[word] += count
			bigrams, junk = _parse_bigram([values['abstract']])			
			for word, count in bigrams.iteritems():
				word_occurrence[word] += count

			for feature in feature_list:
				feature_vec.append(int(word_occurrence[feature]))

			if training_data_label[id_num] == 'Y' or training_data_label[id_num] == '?':
				training_data[example_count:] = feature_vec
				training_target[example_count] = 1
			elif training_data_label[id_num] == 'N':
				training_data[example_count:] = feature_vec
				training_target[example_count] = 0

			word_occurrence = collections.defaultdict(int)
			feature_vec = []
			example_count += 1

	# scikit learn for SVM train
	clf = svm.SVC()
	clf.fit(training_data, training_target)
	return clf

def _train():
	global papers
	global training_data_label
	global log_likelihood
	global log_likelihood_negative

	word_occurrence = collections.defaultdict(int)
	log_likelihood = collections.defaultdict(float)
	word_occurrence_negative = collections.defaultdict(int)
	log_likelihood_negative = collections.defaultdict(float)

	good_count = 0
	bad_count = 0

	tf_idf = collections.defaultdict(float)
	for pmcid, values in papers.iteritems():
		id_num = pmcid[3:]  # remove 'PMC' tag
		if training_data_label[id_num]:
			unigrams, scores = _parse_unigram([values['title']])
			for word, count in scores.iteritems():
				tf_idf[word] += scores[word]
			unigrams, scores = _parse_unigram([values['abstract']])			
			for word, count in scores.iteritems():
				tf_idf[word] += scores[word]

	for pmcid, values in papers.iteritems():
		id_num = pmcid[3:]  # remove 'PMC' tag
		if training_data_label[id_num] == 'Y':
			unigrams, junk = _parse_unigram([values['title']])
			for word, count in unigrams.iteritems():
				word_occurrence[word] += count
			unigrams, junk = _parse_unigram([values['abstract']])			
			for word, count in unigrams.iteritems():
				word_occurrence[word] += count
			good_count += 1
		elif training_data_label[id_num] == '?':  # calling maybe articles as good
			unigrams, junk = _parse_unigram([values['title']])	
			for word, count in unigrams.iteritems():
				word_occurrence[word] += count
			unigrams, junk = _parse_unigram([values['abstract']])			
			for word, count in unigrams.iteritems():
				word_occurrence[word] += count
			good_count += 1
		elif training_data_label[id_num] == 'N':
			unigrams, junk = _parse_unigram([values['title']])	
			for word, count in unigrams.iteritems():
				word_occurrence_negative[word] += count
			unigrams, junk = _parse_unigram([values['abstract']])			
			for word, count in unigrams.iteritems():
				word_occurrence_negative[word] += count
			bad_count += 1

	feature_count = 50
	cur_feature_num = 0

	sorted_tf_idf = sorted(tf_idf.items(), key=operator.itemgetter(1))
	for word, count in reversed(sorted_tf_idf):
		if word_occurrence[word] > 0 and word_occurrence_negative[word] > 0:
			# print word, word_occurrence[word]
			log_likelihood[word] = math.log(float(word_occurrence[word])/good_count)
			log_likelihood_negative[word] = math.log(float(word_occurrence_negative[word])/bad_count)
			cur_feature_num += 1
		if cur_feature_num >= feature_count:
			return

def _svm_test(model):
	global papers
	global test_data_label
	global feature_list

	predictions = collections.defaultdict(str)
	word_occurrence = collections.defaultdict(int)
	feature_vec = []
	for pmcid, values in papers.iteritems():
		id_num = pmcid[3:]  # remove 'PMC' tag
		if test_data_label[id_num]:
			bigrams, junk = _parse_bigram([values['title']])
			for word, count in bigrams.iteritems():
				word_occurrence[word] += count
			bigrams, junk = _parse_bigram([values['abstract']])	
			for word, count in bigrams.iteritems():
				word_occurrence[word] += count

			for feature in feature_list:
				feature_vec.append(int(word_occurrence[feature]))

			predictions[id_num] = model.predict([feature_vec])

		word_occurrence = collections.defaultdict(int)	
		feature_vec = []
	
	tp = 0.0
	tn = 0.0
	fp = 0.0
	fn = 0.0
	for id_num, prediction in predictions.iteritems():
		print predictions[id_num][0]
		if test_data_label[id_num] == 'N' and predictions[id_num][0] == 0:
			tn += 1.0
		elif test_data_label[id_num] in ['?','Y'] and predictions[id_num][0] == 1:
			tp += 1.0
		elif test_data_label[id_num] in ['?','Y'] and predictions[id_num][0] == 0:
			fn += 1.0
		elif test_data_label[id_num] == 'N' and predictions[id_num][0] == 1:
			fp += 1.0
		else:
			raise

	print 'Predictions made : ', len(predictions)
	print 'True negatives : ', (tn + fp)
	print 'Accuracy : ', float(tp+tn)/(tp+tn+fp+fn)
	precision = 0.0 if tp == 0.0 else float(tp)/(tp+fp)
	print 'Precision : ', precision
	recall = float(tp)/(tp+fn)
	print 'Recall : ', recall
	f1 = 2*float(recall*precision/(recall+precision)) if (recall+precision) > 0 else 0
	print 'F1 score : ', f1

def _test():
	global papers
	global test_data_label
	global log_likelihood

	ll = 0
	ll_negative = 0
	predictions = collections.defaultdict(str)
	for pmcid, values in papers.iteritems():
		id_num = pmcid[3:]  # remove 'PMC' tag
		if test_data_label[id_num]:
			unigrams, junk = _parse_unigram([values['title']])
			for word, count in unigrams.iteritems():
				if log_likelihood[word] != 0.0:
					ll += log_likelihood[word]   # TODO use count here?
				if log_likelihood_negative[word] != 0.0:
					ll_negative += log_likelihood_negative[word]
			unigrams, junk = _parse_unigram([values['abstract']])	
			for word, count in unigrams.iteritems():
				if log_likelihood[word] != 0.0:
					ll += log_likelihood[word]
				if log_likelihood_negative[word] != 0.0:
					ll_negative += log_likelihood_negative[word]					
			# if ll < -2 or ll == 0.0:
			if ll > ll_negative or ll == 0.0 or ll_negative == 0.0:			
				predictions[id_num] = '?'
			else:
				predictions[id_num] = 'N'
		ll = 0
		ll_negative = 0

	tp = 0.0
	tn = 0.0
	fp = 0.0
	fn = 0.0
	for id_num, prediction in predictions.iteritems():
		if test_data_label[id_num] == 'N' and predictions[id_num] == 'N':
			tn += 1.0
		elif test_data_label[id_num] in ['?','Y'] and predictions[id_num] == '?':
			tp += 1.0
		elif test_data_label[id_num] in ['?','Y'] and predictions[id_num] == 'N':
			fn += 1.0
		elif test_data_label[id_num] == 'N' and predictions[id_num] == '?':
			fp += 1.0
		else:
			raise

	print 'Predictions made : ', len(predictions)
	print 'True negatives : ', (tn + fp)
	print 'Accuracy : ', float(tp+tn)/(tp+tn+fp+fn)
	precision = float(tp)/(tp+fp)
	print 'Precision : ', precision
	recall = float(tp)/(tp+fn)
	print 'Recall : ', recall
	f1 = 2*float(recall*precision/(recall+precision)) if (recall+precision) > 0 else 0
	print 'F1 score : ', f1

def main(argv):
	global stop_words
	global stem_patterns
	global good_count
	global bad_count
	global unlabeled_count
	global title_list_good
	global title_list_bad
	global abstract_list_good
	global abstract_list_bad
	global labeled_data
	global papers

	papers = collections.defaultdict(dict)
	pmcid = ''
	title = ''
	abstract = ''

	for line in sys.stdin:
		if 'PMC - ' in line:
			if pmcid != '':
				papers[pmcid] = {'title':title, 'abstract':abstract}
			pmcid = line.strip().split(' ')[-1]
			title = ''
			abstract = ''
		elif 'TI  -' in line:
			title = line.strip().split('TI  - ')[-1]
			title += _complete()
		elif 'AB  -' in line:
			abstract = line.strip().split('AB  - ')[-1]
			abstract += _complete()
	papers[pmcid] = {'title':title, 'abstract':abstract}

	title_list_good = []
	title_list_bad = []
	abstract_list_good = []
	abstract_list_bad = []
	good_count = 0
	bad_count = 0
	unlabeled_count = 0

	# for pmcid, values in papers.iteritems():
	# 	if int(pmcid[-1]) in [7,8,9,0]:
	# 		pass
	# 	else:
	# 		print 'PMCID: ' + pmcid
	# 		print 'Title: ' + values['title']
	# 		print 'Abstract: ' + values['abstract']

	_parse_labeled_data()

	for pmcid, values in papers.iteritems():
		if int(pmcid[-1]) in [7,8,9,0]:
			pass
			unlabeled_count += 1
		else:
			id_num = pmcid[3:]  # remove 'PMC' tag
			if labeled_data[id_num] == 'Y':
				title_list_good.append(values['title'])
				abstract_list_good.append(values['abstract'])
				good_count += 1
			elif labeled_data[id_num] == '?':  # calling maybe articles as good
				title_list_good.append(values['title'])
				abstract_list_good.append(values['abstract'])
				good_count += 1
			elif labeled_data[id_num] == 'N':
				title_list_bad.append(values['title'])
				abstract_list_bad.append(values['abstract'])
				bad_count += 1
			else:
				unlabeled_count += 1

	stop_words = []
	for line in open("common_words.txt", 'r'):
		stop_words.append(line.rstrip())

	stem_patterns = []
	for line in open("stems.txt", 'r'):
		stem_patterns.append(line.rstrip())

	# _train()
	# _test()
	model = _svm_train()
	_svm_test(model)
	# _generate_ngrams()

	print 'Good articles : ', good_count
	print 'Bad articles : ', bad_count
	print 'Unlabeled/tableless articles : ', unlabeled_count

if __name__ == '__main__': 
	main(sys.argv)

