

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
