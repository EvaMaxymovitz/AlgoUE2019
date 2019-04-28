from Bio import SeqIO
from Bio.Seq import Seq
from argparse import ArgumentParser
from Bio.Alphabet import generic_dna
import sys


parser = ArgumentParser()
parser.add_argument('--match', default=1,
                    help='score for a match, default = 1')
parser.add_argument('--missmatch', default=-1,
                    help='score for a missmatch, default = -1')
parser.add_argument('--gap', default=-2,
                    help='score for a gap, default = -2')

args = parser.parse_args()

input_seq = SeqIO.parse(sys.stdin, "fasta")

i = 0
for seq in input_seq:
    if i == 0:
        seq_1 = seq.seq
        id_1 = seq.id
    elif i == 1:
        seq_2 = seq.seq
        id_2 = seq.id
    else:
        exit("Please only add 2 Sequences in fasta file")
    i+=1

matrix_score = [[0]]
matrix_path = [[" "]]

nrow = len(seq_1) + 1
ncol = len(seq_2) + 1

for i in range(1,ncol,1):
    matrix_score[0].append(matrix_score[0][i - 1] + args.gap)
    matrix_path[0].append("r")

iterator_1 = 0
iterator_2 = 0

for row in range(1,nrow,1):
    matrix_score.append([matrix_score[row - 1][0] + args.gap])
    matrix_path.append(["u"])
    for col in range(1,ncol,1):
        vertical = matrix_score[row - 1][col] + args.gap
        horizontal = matrix_score[row][col - 1] + args.gap
        
        if (seq_1[iterator_1] == seq_2[iterator_2]):
            diagonal = matrix_score[row - 1][col - 1] + args.match
        else:
            diagonal = matrix_score[row - 1][col - 1] + args.missmatch

        if horizontal >= vertical and horizontal > diagonal:
            matrix_score[row].append(horizontal)
            matrix_path[row].append("r")
        elif vertical > horizontal and vertical > diagonal:
            matrix_score[row].append(vertical)
            matrix_path[row].append("u")
        elif diagonal >= horizontal and diagonal >= vertical:
            matrix_score[row].append(diagonal)
            matrix_path[row].append("d")
        else:
            exit("Error!")
        iterator_2 += 1
    iterator_1 +=1
    iterator_2 = 0

print("Similarity score", matrix_score[len(seq_1)][len(seq_2)], file=sys.stderr)

col = len(matrix_path[0]) - 1
row = len(matrix_path) - 1
matrix_path = ""

while(row > 0 or col > 0):
    if matrix_path[row][col] == "d":
        matrix_path += "d"
        row -= 1
        col -= 1
    elif matrix_path[row][col] == "u":
        matrix_path += "u"
        row -= 1
    elif matrix_path[row][col] == "r":
        matrix_path += "r"
        col -= 1
    elif matrix_path[row][col] == " ":
        break
    else:
        print("Unknown element")
matrix_path = matrix_path[::-1]

alignment = ["","",""]
iterator_1 = 0
iterator_2 = 0
for step in matrix_path:
    if step == "d":
        alignment[0] += seq_1[iterator_1]
        alignment[1] += seq_2[iterator_2]
        if seq_1[iterator_1] == seq_2[iterator_2]:
            alignment[2] += "*"
        else:
            alignment[2] += " "
        iterator_1 += 1
        iterator_2 += 1
    elif step == "u":
        alignment[0] += seq_1[iterator_1]
        alignment[1] += "-"
        alignment[2] += " "
        iterator_1 += 1
    elif step == "r":
        alignment[0] += "-"
        alignment[1] += seq_2[iterator_2]
        alignment[2] += " "
        iterator_2 += 1

rec_1 = SeqIO.SeqRecord(Seq(alignment[0], generic_dna), id_1)

rec_2 = SeqIO.SeqRecord(Seq(alignment[1], generic_dna), id_2)

rec_3 = SeqIO.SeqRecord(Seq(alignment[2]),"")
rec = [rec_1, rec_2, rec_3]


SeqIO.write(rec,sys.stdout, "clustal")