#!/usr/bin/env python

import sys
import collections
import operator
import glob

def _get_tableless_id():
	global tableless_id

	tableless_id = []
	for line in open("no_table_papers.txt", 'r'):
		tableless_id.append(line.strip())

def _parse_labeled_data(filename):
  labeled_terms = collections.defaultdict(str)

  for line in open(filename, 'r'):
    temp = line.strip().split("\t")
    term_count = temp[0]
    label = temp[1].split(" ")[0]
    term = temp[2].strip()
    labeled_terms[term] = label

  return labeled_terms

def main(argv):
  path = "BioNLP-ST_2013_CG_training_data/*.a1"
  all_labeled_terms = collections.defaultdict(str)

  for filename in glob.glob(path):
    # filename = "BioNLP-ST_2013_CG_training_data/PMID-11387198.a1"
    all_labeled_terms.update(_parse_labeled_data(filename))

  for term, label in all_labeled_terms.iteritems():
    print term + "--->" + label


if __name__ == '__main__': 
	main(sys.argv)

