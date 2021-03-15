#py -m pip install pandas
#python -m pip install -U pip pandas
#python -m pip install -U pip xlrd
#python -m pip install -U pip openpyxl
import sys
import shutil
import pandas as pd

script, file_path, file_path_to_copy = sys.argv
text_file = open(file_path, "r")
lines = text_file.readlines()
text_file.close()

for line in lines:
    parts = line.strip().split("_")
    file_name = parts[1] + ".xlsx"
    shutil.copyfile(file_path_to_copy, file_name)
    df = pd.read_excel(file_name, sheet_name = 1)
    df.at['C', 1] = 'WeiChienHsing'
    df.to_excel(file_name, "Sheet1 (2)")




    