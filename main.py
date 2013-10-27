filename = "testInput.txt"
inputFile = open(filename, 'rt')
# State Trans. Table = [eol, letter, digit, period, (~, ?, :, _, \)]
STT = [
    ['noTokenErr', 1, 2, 'floatErr', 'charErr', 0],
    ['F1', 1, 1, 'F1', 'charErr', 'F1'],
    ['F2', 'F2', 2, 3, 'charErr', 'F2'],
    ['floatErr', 'floatErr', 4, 'floatErr', 'charErr', 'floatErr'],
    ['F3', 'F3', 4, 'F3', 'charErr', 'F3']
]


def main():
    #TODO: Add Header
    lineNum = 1
    while True:
        line = inputFile.readline()
        if len(line) == 0:
            break
        token = NextToken(line)
        print("\nLine " + str(lineNum) + " Token: " + repr(token))
        lineNum += 1


def NextToken(inputLine):
    state = 0
    valStart = 0
    for i, ch in enumerate(inputLine):
        chInt = CharToIntCode(ch)
        if chInt == 5:
            valStart += 1
        newState = STT[state][chInt]
        if newState not in {
            'F1', 'F2', 'F3', 'noTokenErr', 'charErr', 'floatErr'
        }:
            state = newState
        elif newState == 'F1':
            #token = (type, value)
            tokenValue = inputLine[(valStart - 1):i].lower()
            if tokenValue in {
                'bool', 'char', 'else', 'false', 'float',
                'if', 'int', 'main', 'true', 'while'
            }:
                tokenType = "keyword"
            else:
                tokenType = "identifier"
            newToken = tokenType, tokenValue
            return newToken
        elif newState == 'F2':
            tokenValue = inputLine[(valStart - 1):i]
            tokenType = "integer"
            newToken = tokenType, tokenValue
            return newToken
        elif newState == 'F3':
            tokenValue = inputLine[(valStart - 1):i]
            tokenType = "float"
            newToken = tokenType, tokenValue
            return newToken
        elif newState == 'noTokenErr':
            tokenValue = "NO TOKEN"
            tokenType = "ERROR"
            newToken = tokenType, tokenValue
            return newToken
        elif newState == 'charErr':
            tokenValue = "ILLEGAL CHARACTER: " + repr(ch)
            tokenType = "ERROR"
            newToken = tokenType, tokenValue
            return newToken
        elif newState == "floatErr":
            tokenValue = "ILLEGAL FLOAT"
            tokenType = "ERROR"
            newToken = tokenType, tokenValue
            return newToken



def CharToIntCode(char):
    testString = char
    # Test for eol/newline char
    if testString == "\\n":
        return 0
    elif testString.isalpha():
        return 1
    elif testString.isdigit():
        return 2
    elif testString == '.':
        return 3
    elif testString in {'~', '?', ':', '_', "\\"}:
        return 4
    else:
        return 5


if __name__ == '__main__':
    main()
