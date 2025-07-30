from Bio.Align.Applications import ClustalwCommandline
from Bio import Phylo
import os

def write_fasta(sequences, output_path):
    from Bio import SeqIO
    SeqIO.write(sequences, output_path, "fasta")

def run_alignment(input_fasta):
    clustalw_exe = "clustalw2"  # or full path like "/usr/bin/clustalw2"
    cline = ClustalwCommandline(clustalw_exe, infile=input_fasta)
    stdout, stderr = cline()
    return input_fasta.replace(".fasta", ".aln"), input_fasta.replace(".fasta", ".dnd")

def build_tree(dnd_file):
    tree = Phylo.read(dnd_file, "newick")
    Phylo.draw(tree)
