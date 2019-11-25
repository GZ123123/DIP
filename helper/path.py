def get_extension(path):
    return path.split('.')[-1]
    
def get_filename(path):
    dir = path.split('/')[-1]
    return ".".join(dir.split(".")[:-1])
