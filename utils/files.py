def read_file(file: str) -> str:
    content = None
    with open(file, 'r') as buf:
        content = buf.read()
    return content