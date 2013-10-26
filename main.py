filename = "givenInput.txt"
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
    index = 1
    state = 0
    while state not in {'F1', 'F2', 'F3'} or state == 0:
        ch = inputFile.read(1)
        if ch == '':
            break
        if ch in {' ', '(', ')', ';', '{', '}', ',', '/', '+', '=', '*'}:
            continue
        state = 0
        print(ch)
        chInt = CharToType(ch)
        newState = STT[state][chInt]
        print("State is: " + str(newState))
        if newState not in {
            'F1', 'F2', 'F3', 'noTokenErr', 'charErr', 'floatErr'
        }:
            state = newState
            #print("State is: " + str(state))
        elif newState in {'F1', 'F2', 'F3'}:
            tokenType = newState
            #print("Final State is: " + str(newState))
            while ch != '\n':
                ch = inputFile.read(1)
            break


def CharToType(char):
    testString = char
    # Test for eol/newline char
    if testString == '\n':
        return 0
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


if __name__ == '__main__':
    main()
