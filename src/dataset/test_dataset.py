'''
@author: xueli
'''
import json
import os
import sys
print(sys.path)
assert False
file = os.path.abspath('../../dataset/processed/patients_mimic3_full.json')
with open(file, 'r') as fp:
    patients = json.load(fp)
visits = patients[0]['visits']
stat_dict = {"patient":0, "visit":0}
keys = ["DXs", "CPTs", "DRGs", "Drugs"]
for key in keys:
    stat_dict[key] = set()
for patient in patients:
    visits = patient['visits']
    stat_dict["patient"] = stat_dict["patient"] + 1
    stat_dict["visit"] = stat_dict["visit"] + len(visits)
    for visit in visits:
        for key in keys:
            stat_dict[key] |= set(visit[key])
print("# patients = " + str(stat_dict["patient"]))
print("# visits = " + str(stat_dict["visit"]))
print("avg visits = " + str(stat_dict["visit"] / stat_dict["patient"]))
for key in keys:
    print(f"# unique {key} = " + str(len(stat_dict[key])))
