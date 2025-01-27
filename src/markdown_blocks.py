def markdown_to_blocks(markdown):
    strp_strings = []    
    block_strings = markdown.split('\n\n')
    for string in block_strings:
        string = string.strip()
        if string != '':
            strp_strings.append(string)
    return strp_strings