def loadHeader(file):
    """
    Args
        file: the http header text file path
    """
    dHeader = {}

    oFile = open(file)
    lList = dict(item.split(':',1) for item in oFile.read().split('\n'))
    oFile.close()
    return lList

if __name__ = '__main__"':
    print(loadHeader('header_file.txt'))
