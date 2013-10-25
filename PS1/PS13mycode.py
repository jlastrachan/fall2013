def reset_table(maxInput, tableSize):
    table = [0]*tableSize
    for i in range(maxInput):
        table[i] = (i,)
    return table

def compress(msg, maxInput, tableSize):
    """
    arguments:
    maxInput       -- a positive integer
    msg            -- a list of integers from range(maxInput)
    tableSize      -- an integer greater than maxInput
    
    outputs: a list of integers from range(tableSize)
    """
    code_table = reset_table(maxInput, tableSize)
    table_index = maxInput
    result_code_msg = []
    string = (msg[0],)
    msg_index = 1
    while msg_index < len(msg):
        #print code_table
        symbol = (msg[msg_index],)
        #print "looking for -- ", string+symbol
        if string + symbol in code_table:
            string = string + symbol
        else:
            result_code_msg.append(code_table.index(string))
            if table_index is tableSize:
                code_table = reset_table(maxInput, tableSize)
                table_index = maxInput
            code_table[table_index] = string + symbol
            table_index += 1
            string = symbol
        msg_index += 1
    result_code_msg.append(code_table.index(string))       

    return result_code_msg

def uncompress(compressed_msg, maxInput, tableSize):
    """
    arguments:
    maxInput       -- a positive integer
    tableSize      -- an integer greater than maxInput
    compressed_msg        -- a list of integers from range(tableSize)

    outputs: a list of integers from range(maxInput)
    """
    code_table = reset_table(maxInput, tableSize)
    code = compressed_msg[0]
    string = code_table[code]
    result_msg = [code_table[code][0]]
    msg_index = 1
    table_index = maxInput
    while msg_index < len(compressed_msg):
        #print "code table -- ", code_table
        code = compressed_msg[msg_index]
        if code >= table_index:
            entry = string + (string[0],)
        else:
            entry = code_table[code]

        for msg in entry:
            result_msg.append(msg)
        
        
        code_table[table_index] = string + (entry[0],)
        table_index += 1
        if table_index is tableSize:
            code_table = reset_table(maxInput, tableSize)
            table_index = maxInput
        
        string = entry
        msg_index += 1
    return result_msg



if __name__ == "__main__": 
    msg = [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0]
    maxInput = 2
    tableSize = 5

    compressed_msg = compress(msg, maxInput, tableSize)
    print "Compressed msg -- ", compressed_msg
    orig_msg = uncompress(compressed_msg, maxInput, tableSize)
    print "Original msg -- ", orig_msg