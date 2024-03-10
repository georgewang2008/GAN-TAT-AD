# -*- coding: utf-8 -*-
"""ISEF Graphs

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l6InQQ6mIR4g2eBimBsaB_qMydpr77ZO
"""

import csv

#Known
known_file = open("gProfiler_known.csv", "r")
known_reader = csv.reader(known_file)

MF_List = []
BP_List = []
KEGG_List = []
REAC_List = []

for row in known_reader:
  if row[0] == "GO:MF":
    MF_List.append(row)
  elif row[0] == "GO:BP":
    BP_List.append(row)
  elif row[0] == "KEGG":
    KEGG_List.append(row)
  elif row[0] == "REAC":
    REAC_List.append(row)
  else:
    continue

#Unknown
unknown_file = open("gProfiler_unknown.csv", "r")
unknown_reader = csv.reader(unknown_file)

Unknown_MF_List = []
Unknown_BP_List = []
Unknown_KEGG_List = []
Unknown_REAC_List = []

for row in unknown_reader:
  if row[0] == "GO:MF":
    Unknown_MF_List.append(row)
  elif row[0] == "GO:BP":
    Unknown_BP_List.append(row)
  elif row[0] == "KEGG":
    Unknown_KEGG_List.append(row)
  elif row[0] == "REAC":
    Unknown_REAC_List.append(row)
  else:
    continue

print(MF_List)

def find_intersection(list1, list2):
    set1 = set(item[1] for item in list1)
    set2 = set(item[1] for item in list2)

    intersection_set = set1.intersection(set2)

    intersection_list1 = [item for item in list1 if item[1] in intersection_set]
    intersection_list2 = [item for item in list2 if item[1] in intersection_set]

    return intersection_list1, intersection_list2

Known_List_MF, Our_Predictions_MF = find_intersection(MF_List, Unknown_MF_List)
Known_List_BP, Our_Predictions_BP = find_intersection(BP_List, Unknown_BP_List)
Known_List_REAC, Our_Predictions_REAC = find_intersection(REAC_List, Unknown_REAC_List)
Known_List_KEGG, Our_Predictions_KEGG = find_intersection(KEGG_List, Unknown_KEGG_List)
print(Our_Predictions_BP)

def pair_lists(A, B):
    dict_B = {}
    for sublist in B:
        key = sublist[1]
        if key in dict_B:
            dict_B[key].append(sublist)
        else:
            dict_B[key] = [sublist]
    result = []
    for sublist in A:
        key = sublist[1]
        if key in dict_B:
            result.extend([[sublist, match] for match in dict_B[key]])
    return result

MF_result = pair_lists(Known_List_MF, Our_Predictions_MF)
BP_result = pair_lists(Known_List_BP, Our_Predictions_BP)
KEGG_result = pair_lists(Known_List_KEGG, Our_Predictions_KEGG)
REAC_result = pair_lists(Known_List_REAC, Our_Predictions_REAC)

print(MF_result)
print(BP_result)

import matplotlib.pyplot as plt

def create_graph(data, cap=None):
    x_values = []
    known_scores = []
    unknown_scores = []

    for idx, sublist in enumerate(data):
        known_score = float(sublist[0][5])
        unknown_score = float(sublist[1][5])

        x_values.append(idx + 1)


        if cap is not None:
            known_score = min(known_score, cap)
            unknown_score = min(unknown_score, cap)

        known_scores.append(known_score)
        unknown_scores.append(unknown_score)

    plt.scatter(x_values, known_scores, color='blue', label='Known Score (Actual)')

    plt.scatter(x_values, unknown_scores, color='orange', label='Unknown Score (Predicted)')

    plt.xlabel('Data Points')
    plt.ylabel('Score')
    plt.title('Known and Unknown Scores')

    plt.legend(loc='upper right')

    plt.xticks(x_values)

    if cap is not None:
        plt.ylim(0, cap+3)

    plt.show()

MF_graph = create_graph(MF_result,50)

BP_graph = create_graph(BP_result,40)

KEGG_graph = create_graph(KEGG_result,25)

REAC_graph = create_graph(REAC_result)