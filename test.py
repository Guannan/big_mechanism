#!/usr/bin/env python

import sys
import collections
import operator

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

# def _get_word(words):
# 	word = None
# 	while word == None:
# 		next_word = 
# 		word = _clean_text(next_word)
# 	return word

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
			word_one = word_one.lower()
			word_two = words[i + 1]
			word_two = _clean_text(word_two)
			word_two = word_two.lower()
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
			word_one = word_one.lower()
			word_two = words[i + 1]
			word_two = _clean_text(word_two)
			word_two = word_two.lower()
			word_three = words[i + 2]
			word_three = _clean_text(word_three)
			word_three = word_three.lower()
			trigram = ' '.join([word_one, word_two, word_three])
			trigrams[trigram] += 1

	return trigrams

def _generate_ngrams():
	unigrams = _parse_unigram(title_list)
	sorted_unigrams = sorted(unigrams.items(), key=operator.itemgetter(1))
	for word, count in reversed(sorted_unigrams):
		print word, str(count)

	unigrams = _parse_unigram(abstract_list)
	sorted_unigrams = sorted(unigrams.items(), key=operator.itemgetter(1))
	for word, count in reversed(sorted_unigrams):
		print word, str(count)

	bigrams = _parse_bigram(title_list)
	sorted_bigrams = sorted(bigrams.items(), key=operator.itemgetter(1))
	for word, count in reversed(sorted_bigrams):
		print word, str(count)

	bigrams = _parse_bigram(abstract_list)
	sorted_bigrams = sorted(bigrams.items(), key=operator.itemgetter(1))
	for word, count in reversed(sorted_bigrams):
		print word, str(count)

	trigrams = _parse_trigram(title_list)
	sorted_trigrams = sorted(trigrams.items(), key=operator.itemgetter(1))
	for word, count in reversed(sorted_trigrams):
		print word, str(count)

	trigrams = _parse_trigram(abstract_list)
	sorted_trigrams = sorted(trigrams.items(), key=operator.itemgetter(1))
	for word, count in reversed(sorted_trigrams):
		print word, str(count)

def main(argv):
	global stop_words
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

	# for pmcid, values in papers.iteritems():
	# 	if int(pmcid[-1]) in [7,8,9,0]:
	# 		pass
	# 	else:
	# 		print 'PMCID: ' + pmcid
	# 		print 'Title: ' + values['title']
	# 		print 'Abstract: ' + values['abstract']

	labeled_data = collections.defaultdict(str)
	for line in open("labeled_preprocessing_data.txt", 'r'):
		temp = line.strip().split(',')
		labeled_data[temp[0]] = temp[1]  # match pmc id with labels Y, ?, N

	for pmcid, values in papers.iteritems():
		if int(pmcid[-1]) in [7,8,9,0]:
			pass
		else:
			id_num = pmcid[3:]  # remove 'PMC' tag
			if labeled_data[id_num] == 'Y':
				title_list_good.append(values['title'])
				abstract_list_good.append(values['abstract'])
			elif labeled_data[id_num] == '?':  # calling maybe articles as good
				title_list_good.append(values['title'])
				abstract_list_good.append(values['abstract'])	
			elif labeled_data[id_num] == 'N':
				title_list_bad.append(values['title'])
				abstract_list_bad.append(values['abstract'])

	# _generate_ngrams()

	stop_words = []
	for line in open("common_words.txt", 'r'):
		stop_words.append(line.rstrip())

	unigrams = _parse_unigram(abstract_list_good)
	sorted_unigrams = sorted(unigrams.items(), key=operator.itemgetter(1))
	for word, count in reversed(sorted_unigrams):
		print word, str(count)

if __name__ == '__main__': 
	main(sys.argv)

