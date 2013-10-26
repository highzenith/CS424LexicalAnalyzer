filename = "givenInput.txt"
inputFile = open(filename, 'rt')

def NextToken(tokenIndex):
    newToken = inputFile.read(tokenIndex)
    return newToken


def main():
    index = 1
    while True:
        token = NextToken(index)
        print(token)
        if token == '':
            break
