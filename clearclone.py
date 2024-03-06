# pip install biopython==1.80
import os
from Bio import SeqIO
 
Info = {}
with open("C:/Users/Bo Lyu/Desktop/Library.csv", "r") as fin:
    lines = fin.readlines()
    lines = lines[1:]
    for line in lines:
        Target_Gene, Symbol_gRNA, Target_Sequence = line.strip().split(",")
        Info[Target_Sequence] = {
            "Target_Gene": Target_Gene,
            "Symbol_gRNA": Symbol_gRNA
        }
 
results = []
for root, dirs, files in os.walk("C:/Users/Bo Lyu/Desktop/seq"):
    for file in files:
        print("********* file:", file)
        left = "TATATATCTTGTGGAAAGGACGAAACACCG"
        right = "GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCCGTTATCAAC"
        handle = open(f"C:/Users/Bo Lyu/Desktop/seq/{file}", "rb")
        sequence = None
        for record in SeqIO.parse(handle, "abi"):
            sequence = str(record.seq)
        if sequence == None:
            print(f"Error: cannot open {file}.")
            exit(0)
        left_pos = sequence.find(left)
        right_pos = sequence.find(right)
        mid = sequence[left_pos + len(left): right_pos]
        print(f"left_pos {left_pos} right_pos {right_pos} mid {mid}")
        
        if left_pos == -1 or right_pos == -1 or mid == None:
            results.append([file, "Left/Right Not Found", "None", "None", "None", "None"])
        else:
            if mid in Info.keys():
                gene_name, guide_name = Info[mid]["Target_Gene"], Info[mid]["Symbol_gRNA"]
            else:
                gene_name, guide_name = "Not In List", "Not In List"
            results.append([file, gene_name, guide_name, mid, left_pos, right_pos])
 
results.sort(key=lambda x:(x[1], x[2]))
with open("./results.csv", "w") as fout:
    fout.write("ab1 file name,gene name,guide number,gene sequence,left pos,right pos\n")
    for result in results:
        fout.write(f"{result[0]},{result[1]},{result[2]},{result[3]},{result[4]},{result[5]}\n")
