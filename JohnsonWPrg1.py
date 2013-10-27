import collections
#Variable containing the filename for input
inFilename = "givenInput.txt"
#Variable containing the filename for output
outFilename = "testOutput.txt"
#Variable for reading text from the input file
inputFile = open(inFilename, 'rt')
#Variable for writing to the output file
outputFile = open(outFilename, 'w')
#String containing the header for output
headingStr = "-Line Number-    -Token Type-            -Token-"
#String containing the header for the symbol table in the output
symbolTblStr = "-Symbol-" + 9 * " " + "-Line Numbers-"
#Dictionary to be used as the symbol table in this lexer
symbolTable = collections.OrderedDict()
# State Trans. Table = [eol, letter, digit, period, (~, ?, :, _, \), Other]
STT = [
    ['noTokenErr', 1, 2, 'floatErr', 'charErr', 0],
    ['F1', 1, 1, 'F1', 'charErr', 'F1'],
    ['F2', 'F2', 2, 3, 'charErr', 'F2'],
    ['floatErr', 'floatErr', 4, 'floatErr', 'charErr', 'floatErr'],
    ['F3', 'F3', 4, 'F3', 'charErr', 'F3']
]


#-----------------------------------------------------------
# In the main function of this program, a line of the input
# file is read and then passed into the NextToken() function.
# After NextToken() returns a token, the details of the
# token, along with the line number is printed. The token is
# also added to the symbol table if it is an identifier type.
# Finally, the symbol table is printed after the tokens.
#-----------------------------------------------------------
def main():
    print("OUTPUT")
    outputFile.write("OUTPUT" + "\n")
    print(headingStr)
    outputFile.write(headingStr + "\n")
    lineNum = 1
    while True:
        line = inputFile.readline()
        if len(line) == 0:
            break
        token = NextToken(line)
        if token[0] is not None:
            if token[0] == "identifier":
                symbolTable.setdefault(token[1], []).append(lineNum)
        print(str(lineNum), end="")
        outputFile.write(str(lineNum))
        print(" " * (17 - len(str(lineNum))), end="")
        outputFile.write(" " * (17 - len(str(lineNum))))
        print(str(token[0]), end='')
        outputFile.write(str(token[0]))
        print(" " * (24 - len(str(token[0]))), end="")
        outputFile.write(" " * (24 - len(str(token[0]))))
        print(str(token[1]))
        outputFile.write(str(token[1]) + "\n")
        lineNum += 1
    print("\n" * 2 + "SYMBOL TABLE")
    outputFile.write("\n" * 2 + "SYMBOL TABLE" + "\n")
    print(symbolTblStr)
    outputFile.write(symbolTblStr + "\n")
    for i in range(0, len(symbolTable)):
        symbol = symbolTable.popitem(last=False)
        print(symbol[0], end="")
        outputFile.write(symbol[0])
        print(" " * (17 - len(str(symbol[0]))), end="")
        outputFile.write(" " * (17 - len(str(symbol[0]))))
        print(symbol[1])
        outputFile.write(str(symbol[1]) + "\n")


#-----------------------------------------------------------
# This function repeatedly parses a character from a line of
# input, checking the indices of the State Transition Table
# to decide the next state. When a Final State or Error is
# detected, a corresponding token is returned to main().
#-----------------------------------------------------------
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


#-----------------------------------------------------------
# This function converts the next character in the file to
# its corresponding int code to be used as an index for the
# State Transition Table.
#-----------------------------------------------------------
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
