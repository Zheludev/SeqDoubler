## a callable script to take an input .fasta, and for each sequence, double it end on

## written by INZ - 11/15/22
## Stanford Unversity
## provided with no acceptance of liability or promise of functionality
## version 0.1.0

import argparse

def main(input_fasta_name, output_fasta_name):
	
	##input_fasta_name = 'Supercluster_001_antisense_MarsCP_111221.fasta'
	input_fasta_file = open(input_fasta_name, mode='r')
	input_fasta_list = input_fasta_file.read().splitlines()
	input_fasta_file.close()
	
	##output_fasta_name = 'Supercluster_001_antisense_MarsCP_doubled_111221.fasta'
	
	for seq_ind in range(1, len(input_fasta_list), 2):
		input_fasta_list[seq_ind] = input_fasta_list[seq_ind]*2
	##
	
	with open(output_fasta_name, mode='wt', encoding='utf-8') as myfile:
		for fasta in input_fasta_list:
			myfile.write(fasta)
			myfile.write('\n')
	##
##

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-iF', type=str, help='input .fasta to be doubled, e.g. "Supercluster_001_antisense_MarsCP_111221.fasta"')
	parser.add_argument('-oF', type=str, help='output .fasta name for doubled sequences e.g. "Supercluster_001_antisense_MarsCP_doubled_111221.fasta"')
	
	args = parser.parse_args()
	main(args.iF, args.oF)
##