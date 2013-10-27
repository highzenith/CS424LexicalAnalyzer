filename = "testInput.txt"
inputFile = open(filename, 'rt')
# STT = [eol, letter, digit, period, (~, ?, :, _, \)]
STT = [
    ['noTokenErr', 1, 2, 0, 'charErr'],
    ['F1', 1, 1, 'F1', 'charErr'],
    ['F2', 'F2', 2, 3, 'charErr'],
    ['floatErr', 'floatErr', 4, 'floatErr', 'charErr'],
    ['F3', 'F3', 4, 'F3', 'charErr']
]


def main():
    line = inputFile.readline()
    token = NextToken(line)
    print(repr(token))
    # print(str(STT[2][0]))


def NextToken(inputLine):
    state = 0
    print("State is: " + str(state))
    while state not in {'F1', 'F2', 'F3'} or state == 0:
        if len(inputLine) == 0:
            print("End of File Reached")
            break
        for i, ch in enumerate(inputLine):
            chInt = CharToIntCode(ch)
            newState = STT[state][chInt]
            print("State is: " + str(newState))
            if newState not in {
                'F1', 'F2', 'F3', 'noTokenErr', 'charErr', 'floatErr'
            }:
                state = newState
            elif newState == 'F1':
                #token = (type, value)
                tokenValue = inputLine[0:i].lower()
                if tokenValue in {
                    'bool', 'char', 'else', 'false', 'float',
                    'if', 'int', 'main', 'true', 'while'
                }:
                    tokenType = "keyword"
                else:
                    tokenType = "identifier"
                newToken = tokenType, tokenValue
                return newToken


def CharToIntCode(char):
    print("Char ->" + str(char) + "<-")
    testString = char
    # Test for eol/newline char
    if testString.isalpha():
        return 1
    elif testString.isdigit():
        return 2
    elif testString == '.':
        return 3
    elif testString in {'~', '?', ':', '_', "\\"}:
        return 4
    else:
        return 0


if __name__ == '__main__':
    main()
