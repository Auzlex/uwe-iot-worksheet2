"""
    Scripted by Charles Edwards
"""
class Node: ## Node Class

    def __init__(self, turple): ## Constructor
        self.left = None        # left node
        self.right = None       # right node
        self.data  = turple     # turple data assigned to current node

    def recursivelyConstructBranch( tree, turple, index = 0 ): # recursive auto branch creator

        # get the letter and full morse code from the turple
        letter = turple[0]
        morse = turple[1]

        # out of range check index
        if index > len(morse)-1:
            index = len(morse)-1

        # get each individual char
        moreseLetter = morse[index]

        # determine if we are going left
        left = (moreseLetter == ".")

        # if we are going left
        if left:
            #print("going left",turple) # debug
            if(not tree is None): # check if the tree is not none if so keep going left (recursive) and increment the morse code char index
                tree.left = Node.recursivelyConstructBranch( tree.left, turple, index + 1 )
            else: # if the node is none then we must create a new node
                #print( "added left", turple )
                tree = Node( turple )
        else:
            #print("going right",turple) # debug

            if(not tree is None): # check if the tree is not none if so keep going right (recursive) and increment the morse code char index
                tree.right = Node.recursivelyConstructBranch( tree.right, turple, index + 1 )
            else: # if the node is none then we must create a new node
                #print( "added right", turple )
                tree = Node( turple )

        # return the tree
        return tree

    def recursivelyFindBranchData( tree, morse, index = 0 ): # recursive find branch data from given morse code

        # if the index is the same length as morse code return the data for the tree
        if index == len(morse):
            #print("RETURNING:",tree.data[0])
            return tree.data[0]

        # out of range check index
        if index > len(morse)-1:
            index = len(morse)-1

        #print(morse[index])

        # get each individual char
        moreseLetter = morse[index]

        # determine if we are going left
        left = (moreseLetter == ".")

        # if we are going left
        if left:     
            if(not tree is None): # check if the tree is not none if so keep going left (recursive) and increment the morse code char index
                #print("going left",tree.data) # debug
                return Node.recursivelyFindBranchData( tree.left, morse, index + 1 )
        else:
            if(not tree is None): # check if the tree is not none if so keep going right (recursive) and increment the morse code char index
                #print("going right",tree.data) # debug
                return Node.recursivelyFindBranchData( tree.right, morse, index + 1 )

    def recursivelyFindAlphabeticalLetter( tree, letter ): # called when we want to search a letter from alphabetically to return a morse code
        if tree is None: # null check tree
            raise Exception( "Invalid letter" )
        else:# if tree is valid
            if letter < tree.data[0]: # determine alphabetical order of letter
                return Node.recursivelyFindAlphabeticalLetter( tree.left, letter ) # search the left trees recursively
            elif letter > tree.data[0]: # determine alphabetical order of letter
                return Node.recursivelyFindAlphabeticalLetter( tree.right, letter ) # search the right trees recursively
            else:
                return tree.data[1] # return the morse code

    def recursivelyInsertAlphabetical(tree, turple): # called when we want to insert a letter into the binary tree alphabetically

        # get the letter and full morse code from the turple
        letter = turple[0]
        morse = turple[1]

        # if the tree is none
        if tree is None:
            # append a new node
            return Node( (letter, morse) )
        else: # if the node is not none then lets attempt to insert missing elements

            if letter < tree.data[0]:  # determine letter ord / ASCII value and perform comparison
                tree.left = Node.recursivelyInsertAlphabetical(tree.left, turple) # perform recurisvely insert
                return tree # return the tree
            elif letter > tree.data[0]:  # determine letter ord / ASCII value and perform comparison
                tree.right = Node.recursivelyInsertAlphabetical(tree.right, turple) # perform recurisvely insert
                return tree # return the tree
            else:
                tree.data =  (letter, morse) # replace tree if same as
                return tree # return the tree

    def print(tree, nest = 0): ## print tree recursively

        # space the elements by how much nesting e.g. how deep in the tree
        for i in range(nest):
            print('  ', end='')

        # null check tree
        if not tree is None:
            print(tree.data) # print the node data

            # print left right branches recursively
            Node.print( tree.left, nest + 1 )
            Node.print( tree.right, nest + 1 )
        else:
            print( "EMPTY" ) # put empty where that nothing exists on a branch

# morse code letters are created left to right from branch top to down
# due to the nature we add them
morseCodeLetters = [  

    # first layer
    ( "E", "." ),
    ( "T", "-" ),

    # second layer
    ( "I", ".." ),
    ( "A", ".-" ),
    ( "N", "-." ),
    ( "M", "--" ),

    # third layer
    ( "S", "..." ),
    ( "U", "..-" ),
    ( "R", ".-." ),
    ( "W", ".--" ),
    ( "D", "-.." ),
    ( "K", "-.-" ),
    ( "G", "--." ),
    ( "O", "---" ),

    # fourth layer :: NOTE 4 nodes are blank
    ( "H", "...." ),
    ( "V", "...-" ),
    ( "F", "..-." ),
    ( "BLANK", "..--" ),

    ( "L", ".-.." ),
    ( "BLANK", ".-.-" ),
    ( "P", ".--." ),
    ( "J", ".---" ),

    ( "B", "-..." ),
    ( "X", "-..-" ),
    ( "C", "-.-." ),
    ( "Y", "-.--" ),

    ( "Z", "--.." ),
    ( "Q", "--.-" ),
    ( "BLANK", "---." ),
    ( "BLANK", "----" ),

    # fifth layer
    ( "5", "....." ),
    ( "4", "....-" ),
    ( "3", "...--" ),
    ( "2", "..---" ),

    ( "+", ".-.-." ),
    ( "1", ".----" ),

    ( "6", "-...." ),
    ( "=", "-...-" ),
    ( "/", "-..-." ),
    
    ( "7", "--..." ),
    ( "8", "---.." ),
    ( "9", "----." ),
    ( "0", "-----" ),

    # task 4 adding missing symbols

    # missing blank nodes
    ( "BLANK", "--..-" ),
    ( "BLANK", "...-." ),
    ( "BLANK", "...-.." ),
    ( "BLANK",".-..-" ),
    ( "BLANK","-.-.-" ),

    ( ".", ".-.-.-" ),
    ( "(", "-.--." ),
    ( "¿", "..-.- " ),

    ( ",", "--..--" ),
    ( ")", "-.--.-" ),
    ( "-", "-....-" ),
    ( "¡", "--...-" ),

    ( "?", "..--." ),
    ( "&", ".-..." ),
    ( "_", "..--.-" ),

    ( "'", ".----." ),
    ( ":", "---..." ),
    ( '"', ".-..-." ),

    ( "!", "-.-.--" ),
    ( ";", "-.-.-." ),
    ( "$", "...-..-" ),
    
]

"""
    Construct Morse Code Binary Tree
"""
print("constructing MORSE tree, standby...") # start making MORSE BT

# root node
root_MorseCodeTree = Node( ("root","r") )

# for every turple in morseCodeLetters
for turple in morseCodeLetters:
    # recursively construct branch
    root_MorseCodeTree = Node.recursivelyConstructBranch( root_MorseCodeTree, turple )

# print the final tree
root_MorseCodeTree.print()

# finish tree construction
print("finished MORSE tree construction\n\n") # finished making MORSE BT

print("constructing ALPHABETICAL tree, standby...") # start making ALPHABETICAL BT

"""
    Construct Alphabetical Binary Tree
"""
# root node
root_AlphabeticalCodeTree = Node( ("root","r") )

# for every turple in morseCodeLetters
for turple in morseCodeLetters:
    # recursively construct branch
    root_AlphabeticalCodeTree = Node.recursivelyInsertAlphabetical( root_AlphabeticalCodeTree, turple )

# print the final tree
root_AlphabeticalCodeTree.print()

print("finished ALPHABETICAL tree construction\n\n") # finished making ALPHABETICAL BT

"""
    Encode && Decode Functions
"""
def encode(text): # called when we want to encode text
    encodedStr = "" # string that will be used for construction of morse code
    for letter in text:
        if letter != " ": # if there is no space char then convert char into morse code and add a space on the end
            encodedStr += str(Node.recursivelyFindAlphabeticalLetter(root_AlphabeticalCodeTree,letter.upper())) + " " 
        else:# else if the char is a space then append a forward slash with a space on the end
            encodedStr += "/ "

    # return encoded string
    return encodedStr[:-1] # chop off the last space

def decode(morse): # called when we want to encode text

    splitData = morse.split(" ") # split the string by spaces
    decodedStr = "" # initiaalize decodeStr with empty string

    # for every chunk in split data 
    for chunk in splitData:
        morse = chunk.strip()
        if morse != "/":  # if the character is not a / then we need to decode this segment
            decodedStr += str(Node.recursivelyFindBranchData(root_MorseCodeTree,morse).lower()) # pass in the morse code binary tree and the morse code to decode and it will recursively decode it
        else:# else add a space
            decodedStr += " "
    
    # return decoded str
    return decodedStr
    
# print("encode result =",encode('.'))
# print("encode result =",encode('('))
# print("encode result =",encode(')'))
# print("encode result =",encode('+'))
# print("encode result =",encode('?'))
# print("encode result =",encode(','))
# print("encode result =",encode('-'))
# print("encode result =",encode('"'))
# print("encode result =",encode(';'))
# print("encode result =",encode(':'))
# print("encode result =",encode('&'))
# print("encode result =",encode('$'))
# print("encode result =",encode('!'))
# print("encode result =",encode("'"))
# print("encode result =",encode('_'))
# print("encode result =",encode('¿'))

# print( decode("..-.-") )

# print("decode result =",decode(".-.-.- -.--. -.--.- .-.-. ..--. --..-- -....- .-..-. -.-.-. ---... .-... ...-..- -.-.-- .----. ..--.- ..-.-"))

#print("encode result =",encode("us us"))
#print("decode result =",decode("..- ... / ..- ..."))

#print("encode result =",encode("dogecoin to the moon"))
#print("decode result =","'"+decode("-.. --- --. . -.-. --- .. -. / - --- / - .... . / -- --- --- -.")+"'")

#print("encode result =",encode("qwertyuiopasdfghjklzxcvbnm1234567890"))
#print("decode result =",decode("--.- .-- . .-. - -.-- ..- .. --- .--. .- ... -.. ..-. --. .... .--- -.- .-.. --.. -..- -.-. ...- -... -. -- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----"))

# some testing
#if decode("--.- .-- . .-. - -.-- ..- .. --- .--. .- ... -.. ..-. --. .... .--- -.- .-.. --.. -..- -.-. ...- -... -. -- .---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----").lower() == "qwertyuiopasdfghjklzxcvbnm1234567890":
    #print("good code mate")
#else:
    #print("bad code mate!")