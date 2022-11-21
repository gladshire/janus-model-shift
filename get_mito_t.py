import os
import subprocess


if __name__ == "__main__":
  for cp in os.listdir("MT_Fasta"):
    if os.path.exists(os.getcwd() + "/" + cp + "Newick.tre.gophy.results.tre"):
      continue
    cpPath = os.getcwd() + "/MT_Fasta/" + cp
    grep_cmd = "grep \">\" " + cpPath + " > " + cp + "taxa.txt"
    print(grep_cmd)
    os.system(grep_cmd)
    sed_cmd = "sed -i \"s/>//g\" " + cp + "taxa.txt"
    print(sed_cmd)
    os.system(sed_cmd)
    px_cmd = "pxtrt -t BestMito226.tre.rr -f " + cp + "taxa.txt > " + cp + "Newick.tre"
    print(px_cmd)
    os.system(px_cmd)
    jan_cmd = "janus -s " + cpPath + " -t " + cp + "Newick.tre" + " -rm -g -ue -ul -w 28 -min 4 > " + cp + "Output.txt"
    print(jan_cmd)
    os.system(jan_cmd)
