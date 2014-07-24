#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#@created: 18.07.2014
#@author: Aleksey Komissarov
#@contact: ad3002@gmail.com

import sys
sys.path.append("/Users/akomissarov/Dropbox/workspace")
sys.path.append("/Users/akomissarov/Dropbox/workspace/PyExp")

from EasyOpMap.models import *
from trseeker.tools.statistics import get_mean


def iter_bng_file(file_name):
	'''
	'''
	with open(file_name) as fh:
		for line in fh:
			if line.startswith("#"):
				continue
			raw_data = line.strip().split()
			data = {}
			if raw_data[0] == '0':
				op_obj = OpticContig()
				op_obj.cid = int(raw_data[1])
				op_obj.length = int(float(raw_data[2]))
				continue

			if raw_data[0] == '1':
				op_obj.sites = [int(round(float(x),0)) for x in raw_data[1:]]
				op_obj.nsites = len(op_obj.sites)
				if op_obj.nsites > 1:
					op_obj.marks = [op_obj.sites[i+1]-x for i,x in enumerate(op_obj.sites[0:-1])]
					op_obj.smarks = [int(round(x/100,0)) for x in op_obj.marks]
				yield op_obj


if __name__ == '__main__':
	
	statistics = {
		"n": 0,
		"total_lenght": 0,
		"sites": [],
		"one_site": 0,
		"one_site_length": 0,
		"ok": 0,
		"ok_length": 0,
		"ok_sites": [],
		"less_100kb": 0,
		"less_100kb_length": 0,

	}

	result = []
	for i, om_obj in enumerate(iter_bng_file("example/jellyfish_1008_bppAdj.bnx")):
		statistics["n"] += 1
		statistics["total_lenght"] += om_obj.length
		if om_obj.nsites < 3:
			statistics["one_site"] += 1
			statistics["one_site_length"] += om_obj.length
			continue

		statistics["sites"].append(om_obj.nsites)

		if om_obj.length < 100000:
			statistics["less_100kb"] += 1
			statistics["less_100kb_length"] += om_obj.length
		else:
			statistics["ok"] += 1
			statistics["ok_length"] += om_obj.length
			statistics["ok_sites"].append(om_obj.nsites)

		result.append(om_obj.smarks)
			
	print "Sorting..."
	result.sort()
	print "Saving..."
	with open("example/sm_parsed.txt", "w") as fh:
		for line in result:
			d = "\t".join(map(str, line))
			fh.write("%s\n" % d)

	print min(statistics["ok_sites"])
	print max(statistics["ok_sites"])
	print get_mean(statistics["ok_sites"])

	print min(statistics["sites"])
	print max(statistics["sites"])
	print get_mean(statistics["sites"])

	# print statistics
