import os
import subprocess


if __name__ == "__main__":
  # Combine mitochondrial fastas into single matrix
  os.system("pxcat -s CP_Fasta/*.fasta -p mt.parts -o mt.matrix")
  # Run janus on mitochondrial supermatrix
  os.system("janus -s mt.matrix -t BestMito226.tre.rr -rm -g -ue -ul -w 28 -min 4 > mitoOutput.txt")
  # Combine chloroplastal fastas into single matrix
  os.system("pxcat -s MT_Fasta/*.fasta -p cp.parts -o cp.matrix")
  # Run janus on chloroplastal supermatrix
  os.system("janus -s cp.matrix -t BestChloroplast226.tre.rr -rm -g -ue -ul -w 28 -min 4 > chloroOutput.txt")
