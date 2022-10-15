def add_newline(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    text = text.replace('.', '.\n')
    with open(file_name, 'w') as f:
        f.write(text)


add_newline('letter.txt')
