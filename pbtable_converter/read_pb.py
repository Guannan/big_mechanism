#!/usr/bin/env python


import table_pb2
import sys
import protobuf_json
import json

def ListColumns(table):
	for column in table.column:
		header = column.header.data
		print 'Column header : ', header
		for data in column.data:
			try:
				print 'Data : ', data.data
			except Exception:
				pass


if len(sys.argv) != 2:
	print "Usage: ", sys.argv[0], "TABLE_FILE"
	sys.exit(-1)

table = table_pb2.Table()

f = open(sys.argv[1], "rb")
table.ParseFromString(f.read())
f.close()

# ListColumns(table)
json_obj = protobuf_json.pb2json(table)
print 'Rows: ', len(table.column[0].data)
print 'Columns : ', len(table.column)
# print str(json_obj)
parsed = json.loads(json.dumps(json_obj))
print json.dumps(parsed, indent=4, sort_keys=True)
# print json_obj

