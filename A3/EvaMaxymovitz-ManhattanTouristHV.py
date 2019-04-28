#!/bin/bash

# Programm aufrufen:
#       - EvaMaxymovitz-ManhattanTouristHV.py < rmHV_10_3
#       - EvaMaxymovitz-ManhattanTouristHV.py < rmHV_999_3

# Your pull request should include the following:
#         - your program (source code)
#         - wheight of the longest path for your input files (one for dim 10, and one for dim 999, 
#             respectively)
#         - two input files you selected. Let me know which file you chose in your ping message, 
#             e.g. @mtw please review rmHV_10_5


import sys

Matrix = sys.stdin              # um die Daei aus dem Terminal einzulesen 
List = []                       # Matrix wird als (nested) List gespeichert 

for row in Matrix.readlines():  # Abstände und absätze werden gelöscht, durch tab getrennt
        weight = row.strip("  ").strip(" \n").split("   ") 
        
        if (len(weight) > 1):
            List.append(weight)

dimension = len(List[0])

Matrix_sum={}                   # Matrix, in der Werte gespeichert werden.
for i in range(dimension):
    Matrix_sum[i]=[]
    for j in range(dimension):
        Matrix_sum[i].append(0) # mit 0 befüllen 

for i in range(dimension-1):    # rechter Wert = right 
    Matrix_sum[0][i+1] = Matrix_sum[0][i] + float(List[dimension-1][i])

for i in range(dimension-1):    # unterer Wert = down 
    Matrix_sum[i+1][0] = Matrix_sum[i][0] + float(List[i][0])

for j in range(dimension-1):       
        for i in range(dimension-1):                            # Werte berechnen
                down = Matrix_sum[j][i+1]+ float(List[j][i+1])
                right = Matrix_sum[j+1][i]+ float(List[dimension+j][i])

                if (down > right):                              # höherer Wert wird übernommen
                        Matrix_sum[j+1][i+1] = round(down, 2)   # 2 Nachkommastellen
                else:
                        Matrix_sum[j+1][i+1] = round(right, 2)

print(Matrix_sum[dimension-1][dimension-1])