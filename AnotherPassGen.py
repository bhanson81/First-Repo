import random

def generatepass_word(pwlength):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    pass_words = [] 

    for i in pwlength:
        
        pass_word = "" 
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            pass_word = pass_word + alphabet[next_letter_index]
        
        pass_word = replaceWithNumber(pass_word)
        pass_word = replaceWithUppercaseLetter(pass_word)
        
        pass_words.append(pass_word) 
    
    return pass_words


def replaceWithNumber(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
        return pword


def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
        return pword



def main():
    
    numpass_words = int(input("Num passwords to generate: "))
    
    print("Generating " +str(numpass_words)+" passwords")
    
    pass_wordLengths = []

    print("Minimum length of pass_word should be 3")

    for i in range(numpass_words):
        length = int(input("Enter the length of pass_word #" + str(i+1) + " "))
        if length<3:
            length = 3
        pass_wordLengths.append(length)
    
    
    pass_word = generatepass_word(pass_wordLengths)

    for i in range(numpass_words):
        print ("pass_word #"+str(i+1)+" = " + pass_word[i])



main()
