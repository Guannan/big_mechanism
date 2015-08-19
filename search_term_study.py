#!/usr/bin/env python

import sys
import collections

def main(argv):

	papers = collections.defaultdict(dict)
	pmcids = []

	pmcid = ''
	for line in sys.stdin:
		if 'PMC - ' in line:
			if pmcid != '':
				pmcids.append(pmcid)
			pmcid = line.strip().split(' ')[-1]
	pmcids.append(pmcid)

	pmcids_table = []
	for line in open('search_term_pmcid_collection/pmcid_phosphoproteomics_ras_table_tables_supptable.txt', 'r'):
		pmcids_table.append(line.strip())

	pmcids_notable = []
	for pmcid in pmcids:
		if int(pmcid[-1]) in [3,4,7,8,9,0]:  # neglecting 3/4 no data from Vincent
			pass
		else:
			id_num = pmcid[3:]  # remove 'PMC' tag
			# print 'PMCID: ' + id_num
			if id_num not in pmcids_table:
				pmcids_notable.append(id_num)

	tableless_id = []
	for line in open("no_table_papers.txt", 'r'):
		tableless_id.append(line.strip())

	tableless_match = []
	for pmcid in tableless_id:
		if pmcid in pmcids_notable:
			tableless_match.append(pmcid)
	# print len(tableless_match)  # all mark no tables filtered out

	left = []
	for pmcid in pmcids_notable:
		if pmcid not in tableless_id:
			left.append(pmcid)
			print pmcid

if __name__ == '__main__': 
	main(sys.argv)

