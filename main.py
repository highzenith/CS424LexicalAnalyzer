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


def NextToken():
    state = 0
    while state not in {'F1', 'F2', 'F3'} or state == 0:
        inputLine = inputFile.readline()
        for i, ch in enumerate(inputLine):
            if ch == '':
                print("End of File Reached")
                break
            if ch in {' ', '(', ')', ';', '{', '}', ',', '/', '+', '=', '*'}:
                continue
            chInt = CharToIntCode(ch)
            newState = STT[state][chInt]
            print("State is: " + str(newState) + " chInt is: " + str(chInt))
            if newState not in {
                'F1', 'F2', 'F3', 'noTokenErr', 'charErr', 'floatErr'
            }:
                state = newState
            else:
                state = newState


def CharToIntCode(char):
    testString = char
    # Test for eol/newline char
    if testString == '\n':
        return 0
        print("newline")
    elif testString.isalpha():
        return 1
    elif testString.isdigit():
        return 2
    elif testString == '.':
        return 3
    elif testString in {'~', '?', ':', '_', "\\"}:
        return 4


def main():
    NextToken()
    #print(str(STT[2][0]))


if __name__ == '__main__':
    main()
