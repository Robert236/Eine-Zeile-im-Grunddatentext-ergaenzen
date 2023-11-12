
new_text_line = ';/;Kommission Firma Beispiel!\n'

with open('Beispieldaten.csv', 'r') as csv_file_input:
    with open('data.txt', 'w') as txt_file:
        text_block = []
        block_number = None
        for i, line in enumerate(csv_file_input):
            if i == 0:
                txt_file.write(line)
            else:
                if line[1] != '/':
                    block_number = line
                    if len(text_block) == 0:
                        text_block.append(line)
                    else:
                        text_block.insert(1, new_text_line)
                        for line2 in text_block:
                            txt_file.write(line2)
                        text_block.clear()
                        text_block.append(line)
                elif line[1] == '/':
                    if block_number in text_block:
                        text_block.append(line)

        text_block.insert(1, new_text_line)
        for line3 in text_block:
            txt_file.write(line3)

with open('output_file.csv', "w") as csv_file_output:
    data = open('data.txt', 'r')
    for line in data:
        csv_file_output.write(line)
