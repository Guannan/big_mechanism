#!/usr/bin/env python

import sys
import collections
import operator
import random
import math

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
	chars_to_remove = ['.', ',', '?', '!', '*', '(', ')']
	word = word.translate(None, ''.join(chars_to_remove))
	word = word.lower()
	if word in stop_words:
		return None
	if 'http' in word:
		return None
	return word

def _parse_unigram(text_list):
	"""
	Returns a dictionary of unigrams
	with the keys being the words and 
	the columns being the occurrences
	"""
	unigrams = collections.defaultdict(int)

	for text in text_list:
		words = text.strip().split(' ')
		for i in xrange(len(words)):
			word = words[i]
			temp = _clean_text(word)  # TODO optimize
			if temp != None:
				word = temp
				unigrams[word] += 1

	return unigrams

def _parse_bigram(text_list):
	"""
	Returns a dictionary of bigrams
	with the keys being the words and 
	the columns being the occurrences
	"""
	bigrams = collections.defaultdict(int)

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

	return bigrams

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

def _parse_labeled_data():
	global labeled_data
	global training_data_label
	global test_data_label

	random.seed()
	labeled_data = collections.defaultdict(str)
	training_data_label = collections.defaultdict(str)
	test_data_label = collections.defaultdict(str)

	for line in open("labeled_preprocessing_data.txt", 'r'):
		temp = line.strip().split(',')
		labeled_data[temp[0]] = temp[1]  # match pmc id with labels Y, ?, N
		num = random.randint(0,99)
		if num > 33:  # 1 and 2 divide
			test_data_label[temp[0]] = temp[1]
		else:
			training_data_label[temp[0]] = temp[1]

def _train():
	global papers
	global training_data_label
	global log_likelihood

	word_occurrence = collections.defaultdict(int)
	log_likelihood = collections.defaultdict(float)

	good_count = 0
	for pmcid, values in papers.iteritems():
		id_num = pmcid[3:]  # remove 'PMC' tag
		if training_data_label[id_num] == 'Y':
			unigrams = _parse_unigram([values['title']])
			for word, count in unigrams.iteritems():
				word_occurrence[word] += count
			unigrams = _parse_unigram([values['abstract']])			
			for word, count in unigrams.iteritems():
				word_occurrence[word] += count
			good_count += 1
		elif training_data_label[id_num] == '?':  # calling maybe articles as good
			unigrams = _parse_unigram([values['title']])	
			for word, count in unigrams.iteritems():
				word_occurrence[word] += count
			unigrams = _parse_unigram([values['abstract']])			
			for word, count in unigrams.iteritems():
				word_occurrence[word] += count
			good_count += 1

	feature_count = 100
	cur_feature_num = 0
	sorted_word_occurrence = sorted(word_occurrence.items(), key=operator.itemgetter(1))
	for word, count in reversed(sorted_word_occurrence):
		log_likelihood[word] = math.log(float(count)/good_count)
		cur_feature_num += 1
		if cur_feature_num >= feature_count:
			return
		print word, log_likelihood[word]

def _test():
	global papers
	global test_data_label
	global log_likelihood

	ll = 0
	predictions = collections.defaultdict(str)
	for pmcid, values in papers.iteritems():
		id_num = pmcid[3:]  # remove 'PMC' tag
		if test_data_label[id_num]:
			unigrams = _parse_unigram([values['title']])
			for word, count in unigrams.iteritems():
				if log_likelihood[word] > 0 or log_likelihood[word] < 0:
					ll += log_likelihood[word]   # TODO use count here?
			unigrams = _parse_unigram([values['abstract']])	
			for word, count in unigrams.iteritems():
				if log_likelihood[word] > 0 or log_likelihood[word] < 0:
					ll += log_likelihood[word]
			if ll < -2:
				predictions[id_num] = 'N'
			else:
				predictions[id_num] = '?'
		ll = 0

	correct = 0
	for id_num, prediction in predictions.iteritems():
		if test_data_label[id_num] == 'N' and predictions[id_num] == 'N':
			correct += 1
		elif test_data_label[id_num] == '?' and predictions[id_num] == '?':
			correct += 1
		elif test_data_label[id_num] == 'Y' and predictions[id_num] == '?':
			correct += 1

	print 'Predictions made : ', len(predictions)
	print 'Test dataset size : ', len(test_data_label)
	print 'Accuracy : ', float(correct)/len(predictions)
	print len(log_likelihood)

def main(argv):
	global stop_words
	global good_count
	global bad_count
	global unlabeled_count
	global title_list_good
	global title_list_bad
	global abstract_list_good
	global abstract_list_bad
	global labeled_data
	global papers
	global log_likelihood

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

	_train()
	_test()
	# _generate_ngrams()

	print 'Good articles : ', good_count
	print 'Bad articles : ', bad_count
	print 'unlabeled_count : ', unlabeled_count

if __name__ == '__main__': 
	main(sys.argv)

