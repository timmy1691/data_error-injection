# from generators import *
import src.methods.spelling as spell
import random
import numpy as np
import pandas as pd
import math

from src.generators.key_errors import KEY_NEIGHBORS as kn
from src.generators.key_errors import unicode_mindfuck as um

class editor:
    
    def __init__(self):
        self.originalDataset = None
        self.newDataset = None
        self.errorType = set()

    def dataCheck(self, dataframe):
        if self.originalDataset is None:
            self.originalDataset = dataframe.copy()

    
    def updateErrorType(self, errorType):
        self.errorType.add(errorType)

    
    def retrieveErrorTypes(self):
        return self.errorType


    def addError(self, dataframe, errorType, legend, inst_level = True, ratio=0.2, error_rate=0.1):
        """
        Add error
        error_type  :    type of error
        ratio       :    max proportion of dtaa that contains error
        error_rate  :    Probabuility to conatin error in a certain data value
        """
        self.dataCheck(dataframe)

        if errorType.lower() == "spelling" and inst_level:
            self.errorType.add(errorType.lower()+"_inst")
            self.addSpellingError(dataframe, ratio, error_rate)
        
        elif errorType.lower() == "spelling" and not inst_level:
            self.updateErrorType(errorType.lower()+"_col")
            self.colSpellingError(dataframe, ratio, error_rate, legend=legend)

        elif errorType.lower() == "characters" and inst_level:
            self.updateErrorType("errorType" + "_inst")
            self.addRandomUniChars(dataframe)
            
        elif errorType.lower() == "characters" and not inst_level:
            self.updateErrorType(errorType.lower()+"_col")
            self.addRandomUniChars()

        elif errorType.lower() == "generational":
            pass
        else:
            pass

        return self.newDataset
                

    def addSpellingError(self, dataframe, ratio, error_rate, legend):


        if legend == "keyError":
            from src.generators.key_errors import KEY_NEIGHBORS as legend

        elif legend == "unicode":
            from src.generators.key_errors import unicode_mindfuck as legend

        newDataset = dataframe.copy()

        columns = list(dataframe.columns)
        num_dpoints, _ = dataframe.shape

        for col in columns:
            error_index = list(np.random.choice(range(num_dpoints), size=math.ceil(num_dpoints*ratio)))
            temp_data = dataframe[col]
            temp_data = temp_data.dropna()

            is_string = temp_data.apply(lambda x: isinstance(x, str))
            # is_number = df["col"].apply(lambda x: isinstance(x, numbers.Number))
            if is_string.all():
                # key error
                for index in error_index:
                    val = dataframe.iloc[index][col]
                    new_val = val
                    if val is np.NaN:
                        continue
                    else:
                        num_chars = len(val)
                    
                    randomRate = np.random.sample(size = num_chars)
                    indices = []
                    new_vals = []
                    for i, randomRate in enumerate(randomRate):
                        if randomRate < error_rate:
                            try:
                                new_vals.append(random.choice(legend[val[i].lower()]))
                            except KeyError:
                                new_vals.append(val[i])
                            indices.append(i)
                    new_string = spell.string_replacer(val, indices, new_vals)
                newDataset = self.newDataset.iloc[index][col] = new_string
            self.newDataset = newDataset.copy()

        return self.newDataset
    
    def colSpellingError(self, dataframe, ratio, error, legend):

        if legend == "keyError":
            from src.generators.key_errors import KEY_NEIGHBORS as legend

        elif legend == "unicode":
            from src.generators.key_errors import unicode_mindfuck as legend
        newDataset = dataframe.copy()

        cols = list(dataframe.columns)
        num_cols = len(cols)
        sample_indices = np.random.choice(range(num_cols), size=math.ceil(num_cols*ratio))
        mapper = {}
        for index in sample_indices:
            col_name = cols[index]
            num_chars = len(col_name)
            errorIndex = np.random.choice(range(num_chars), size=math.ceil(num_chars*error))
            change_indices = []
            change_vals = []
            for char_id in sorted(errorIndex):
                    change_indices.append(char_id)
                    change_vals.append(random.choice(legend[col_name[char_id].lower()]))
            
            # print("old col : ", col_name)
            new_col = spell.string_replacer(col_name, change_indices, change_vals)
            # print("new col : ", new_col)

            mapper[col_name] = new_col

        self.newDataset = newDataset.rename(columns = mapper).copy()
        return self.newDataset
    
    def changeColNames(self, dataframe, proportion=0.1, model="wordnet"):

        newDataset = dataframe.copy()
        if model =="wordnet":
            from src.methods.text import col_synonyms_wn as model
        else:
            from src.methods.text import col_synonyms_slm as model

        mapper = {}
        columns = list(dataframe.columns)
        for colname in columns:
            newColname = model(colname)
            mapper[colname] = newColname

        self.newDataset = newDataset.rename(columns=mapper)
        return self.newDataset
        
    def addCharstoCols(self, dataframe, proportion=0.1, location="end"):
        newDataset = dataframe.copy()
        cols = list(dataframe.columns)
        mapper = {}
        from src.generators.key_errors import top_emojis as emotes

        for col in cols:
            if location == "end":
                new_col = col + np.random.choice(emotes, size=2)
            elif location == "start":
                new_col = col + np.random.choice(emotes, size=2)
            else:
                new_col = col
            mapper[col] = new_col
        
        self.newDataset = newDataset.rename(cols=mapper)
        return self.newDataset
            

    def addRandomUniChars(self, dataframe, location="end", proportion=0.1):
        from src.generators.key_errors import top_emojis as emotes
        newDataframe = dataframe.copy()
        columns = list(dataframe.columns)

        num_dp, _ = newDataframe.shape
           
        for col in columns:
            temp_data = dataframe[col]
            temp_data = temp_data.dropna()
            is_string = temp_data.apply(lambda x: isinstance(x, str))
            insert_locs = np.random.choice(range(num_dp), size=math.ceil(num_dp*proportion))
            random_vals = [np.random.choice(range(10), size=1) for num in insert_locs]
            insert_vals = [np.random.choice(emotes, size=val, replace=True) for val in random_vals]
            if is_string.all():
                if location == "end":
                    new_temp_data = spell.insert_end(temp_data, insert_vals, insert_locs)
                newDataframe[col] = new_temp_data
        
        return newDataframe
    
    def commit_file(self, filePath):
        file_type = filePath.split(".")[-1]
        if file_type == "csv":
            self.newDataset.to_csv(filePath)
        elif file_type == "parquet":
            self.newDataset.to_parquet(filePath)
        elif file_type == "json":
            self.newDataset.to_json(filePath)
        else:
            raise ValueError("We do not handle this file type")


    def getPreviousData(self):
        return self.originalDataset
