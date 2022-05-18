#Scott West
#Cipher Project
#Section A01
#12/03/2018


def getHawkIDs():
    return ['scottwest']


def shiftEncrypt(plainText, shift):
    cipher = 'abcdefghijklmnopqrstuvwxyz \';.?,'
    shifted = ''
    for letter in plainText:
        # x corresponds to letter in cipher
        for x in cipher:
            if letter == x:
                # Check if current index is within bounds of cipher
                boundsCheck = cipher.index(x) + shift
                # If index is out of bounds, wrap to beginning of cipher and concatenate letter at index
                # This should allow for a complete 0 - 31 shift for ANY character in the cipher without
                # needing to manually double the length of the cipher
                if boundsCheck > len(cipher) - 1:
                    shifted += cipher[boundsCheck - len(cipher)]
                # Within bounds, concatenate letter at index
                else:
                    shifted += cipher[boundsCheck]
    # Return shifted string
    return shifted


def shiftDecrypt(plainText, shift):
    cipher = 'abcdefghijklmnopqrstuvwxyz \';.?,'
    shifted = ''
    for letter in plainText:
        # x corresponds to letter in cipher
        for x in cipher:
            if letter == x:
                # Check if current index is within bounds of cipher
                boundsCheck = cipher.index(x) - shift
                # If index is out of bounds, wrap to end of cipher and concatenate letter at index
                if boundsCheck < 0:
                    shifted += cipher[boundsCheck + len(cipher)]
                # Within bounds, concatenate letter at index
                else:
                    shifted += cipher[boundsCheck]
    # Return shifted string
    return shifted


# Helper function
def listFromString(aString):
    strungOutList = []
    # Initialize to first index of aString
    i = 0
    # While i is less than the length of aString, append current i
    # to strungOutList
    # Also, while loops are the real MVP...
    while i < len(aString):
        strungOutList.append(aString[i])
        i += 1
    return strungOutList


def MultiAlphaCipher(theKeys, plainFile):
    # line[i] = line0, line1, line2
    line = []

    # Block 1 SampleKeys.txt
    # Open file for read
    fileKeys = open(theKeys, 'r')
    for lineTxt in fileKeys:
        line.append(lineTxt.rstrip())
    fileKeys.close()

    # use the listFromString helper function
    key0, key1, key2 = listFromString(line[0]), listFromString(line[1]), listFromString(line[2])
    # contents of plainFile, each lineTxt is a new index
    fileContents = []

    # Block 2 plainFile.txt
    # Open file for read
    filePlain = open(plainFile, 'r')
    for lineTxt in filePlain:
        fileContents.append(lineTxt.rstrip())
    filePlain.close()

    plainText = 'abcdefghijklmnopqrstuvwxyz \';.?,'
    trackRows = -1
    cycleKeys = 0

    # Block 3 cipherText.txt
    # Open file for write, if file does not exist, creates it
    fileCipher = open('cipherText.txt', 'w')
    for row in fileContents:
        trackRows += 1
        # write a new lineTxt char to file after encrypting each index within fileContents
        if trackRows >= 1:
            fileCipher.write('\n')
        for char in row:
            # while iterating through row(s), cycleKeys will cycle through
            # the indices 0, 1, 2, 0, 1, 2...
            # use key1
            if cycleKeys == 0:
                # write char as char.lower() to convert all capital letters to lowercase
                # SampleKeys.txt does not contain any capitalized characters
                fileCipher.write(key0[plainText.index(char.lower())])
                cycleKeys += 1
            # use key2
            elif cycleKeys == 1:
                fileCipher.write(key1[plainText.index(char.lower())])
                cycleKeys += 1
            # use key3
            else:
                fileCipher.write(key2[plainText.index(char.lower())])
                cycleKeys = 0
    fileCipher.close()


def MultiAlphaDecipher(theKeys, cipherFile):
    # line[i] = line0, line1, line2
    line = []

    # Block 1 SampleKeys.txt
    # Open file for read
    fileKeys = open(theKeys, 'r')
    counterTot = 0
    counterChk = 0
    # implemented loops to selectively remove '\n' chars using lineTxt.rstrip() from
    # each lineTxt (excluding the last lineTxt), new lineTxt chars cause text to decrypt incorrectly
    # Initialize counterTot to number of lines in fileKeys
    for lineTxt in fileKeys:
        counterTot += 1
        if counterChk < counterTot:
            # removes \n char
            line.append(lineTxt.rstrip())
            counterChk += 1
        else:
            line.append(lineTxt)
            counterTot = 0
            counterChk = 0
    fileKeys.close()

    # use the listFromString helper function
    key0, key1, key2 = listFromString(line[0]), listFromString(line[1]), listFromString(line[2])
    # contents of cipherFile, each lineTxt is a new index
    fileContents = []

    # Block 2 cipherText.txt
    # Open file for read
    fileEncrypted = open(cipherFile, 'r')
    # Reinitialize counterTot to number of lines in fileEncrypted
    for lineTxt in fileEncrypted:
        counterTot += 1
        if counterChk < counterTot:
            # removes \n char
            fileContents.append(lineTxt.rstrip())
            counterChk += 1
        else:
            fileContents.append(lineTxt)
    fileEncrypted.close()

    plainText = 'abcdefghijklmnopqrstuvwxyz \';.?,'
    trackRows = -1
    cycleKeys = 0

    # Block 3 plainText.txt
    # Open file for write, if file does not exist, creates it
    fileDecipher = open('MyDecryptedText.txt', 'w')
    for row in fileContents:
        trackRows += 1
        # write a new lineTxt char to file after encrypting each index within fileContents
        if trackRows >= 1:
            fileDecipher.write('\n')
        for char in row:
            # while iterating through row(s), cycleKeys will cycle through
            # the indices 0, 1, 2, 0, 1, 2...
            # use key1
            if cycleKeys == 0:
                # write char as char.lower() to convert all capital letters to lowercase
                # SampleKeys.txt does not contain any capitalized characters
                fileDecipher.write(plainText[key0.index(char.lower())])
                cycleKeys += 1
            # use key2
            elif cycleKeys == 1:
                fileDecipher.write(plainText[key1.index(char.lower())])
                cycleKeys += 1
            # use key3
            else:
                fileDecipher.write(plainText[key2.index(char.lower())])
                cycleKeys = 0
    fileDecipher.close()


# shiftEncrypt('scooter', 29)
# shiftDecrypt('p,llqbo', 29)
# MultiAlphaCipher('SampleKeys.txt', 'plainFile.txt')
# MultiAlphaDecipher('SampleKeys.txt', 'cipherText.txt')

# This was fun.