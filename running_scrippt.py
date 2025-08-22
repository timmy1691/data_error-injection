import pandas as pd 
import numpy as np 
import random 
import numbers
from src.editor import editor

from src.generators.key_errors import KEY_NEIGHBORS as kn
import src.methods.spelling as spell


dataframe = pd.read_csv("datasets/adult.csv")

columns = list(dataframe.columns)

proportion = 0.2
error_rate=0.1

error_type = "spelling"

edit = editor()
res_dataframe = edit.addError(dataframe,error_type,False, proportion, error_rate)
print("original data columns : ", edit.originalDataset.columns)

print("edit column names ", res_dataframe.columns)





# num_dpoints, _ = dataframe.shape

# for col in columns:
#     error_index = list(np.random.choice(range(num_dpoints), size=int(num_dpoints*proportion)))
#     temp_data = dataframe[col]
#     temp_data = temp_data.dropna()

#     is_string = temp_data.apply(lambda x: isinstance(x, str))
#     # is_number = df["col"].apply(lambda x: isinstance(x, numbers.Number))
#     if is_string.all():
#         # key error
#         if error_type == "spelling":
#             for index in error_index:
#                 val = dataframe.iloc[index][col]
#                 new_val = val
#                 if val is np.NaN:
#                     continue
#                 else:
#                     num_chars = len(val)
                
#                 randomRate = np.random.sample(size = num_chars)
#                 indices = []
#                 new_vals = []
#                 for i, randomRate in enumerate(randomRate):
#                     if randomRate < error_rate:
#                         try:
#                             new_vals.append(random.choice(kn[val[i].lower()]))
#                         except KeyError:
#                             new_vals.append(val[i])
#                         indices.append(i)
#                 new_string = spell.string_replacer(val, indices, new_vals)
#             dataframe.iloc[index] = new_string

#             print("old value ", val)
#             print("new val", new_string)


