

def string_replacer(string, indices, new_values):
    new_string = "" 
    num_indices = len(indices)
    for i, index in enumerate(indices):
        if i == 0:
            new_string += string[:index] + new_values[i]
        
        elif i == num_indices-1:
            new_string += new_values[i] + string[index:]
        else:
            new_string += string[indices[i-1]:indices[i]] + new_values[i]
    return new_string


def insert_start(dataframe, values, indices):
    newDataframe = dataframe.copy()
    for index in indices:
        old_val = dataframe[indices[i]]
        new_val = values[i] + old_val
        newDataframe[indices[i]] = new_val
    
    return newDataframe

def insert_end(dataframe, values, indices):
    newDataframe = dataframe.copy()
    for i in range(len(indices)):
        old_val = dataframe[indices[i]]
        new_val = old_val + values[i]
        newDataframe[indices[i]] = new_val
    
    return newDataframe
    
def insert_mid(dataframe, values, indices):
    newDataset = dataframe.copy()
    for i in range(indices):
        old_val = dataframe[indices[i]]
        random_insertion_loc = np.random.choice(len(old_val), size=1)
        new_val = old_val[:random_insertion_loc] + values[i] + old_val[random_insertion_loc:]
        newDataset[indices[i]] = new_val
    return newDataset
