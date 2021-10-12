import random

def rand_word_gen(lang):
    myline_1 = 0
    myline_2 = 0
    #myline_1 is the first word
    #myline_2 is the second word
    #we're adding the first word to myline_2
    if lang=="1":
        file_1=open("wordsENG.txt","r")
        file_2=open("wordsENG2.txt","r")
    elif lang=="2":
        file_1=open("wordsRO.txt","r")
        file_2=open("wordsRO2.txt","r")
    lines = file_1.read().splitlines()
    myline_1 =random.choice(lines)

    lines2 = file_2.read().splitlines()

    if rand_num_gen()%2 == 0:
        myline_1 = myline_1.upper()

    if rand_num_gen()%3 == 0:
        myline_2 = myline_1 + random.choice(lines2)
    elif rand_num_gen()%3 == 2:
        myline_2 = myline_1
    else:
        myline_2 = random.choice(lines2) + myline_1
    return myline_2

def rand_symb_gen():
	lines = open('symbols.txt').read().splitlines()
	myline_1 = random.choice(lines)
	return str(myline_1)

# generate ran number, max 4 digits
def rand_num_gen():
	return random.randint(1,1000)

###########################
def gen_word_and_number(lang):
	rw=str(rand_word_gen(lang))
	rn=str(rand_num_gen())
	return rw,rn

# main function #######################################
def easy_pass_gen(lang):
	randomWord, randomNumber = gen_word_and_number(lang)
	if rand_num_gen()%2 == 0:
		easypass = randomWord + str(randomNumber)
	else:
		easypass = str(randomNumber) + randomWord
	return easypass

def strong_pass_gen(lang):
    temppass = rand_symb_gen()
    for i in range(rand_num_gen()%4):
        symbol = rand_symb_gen()
        temppass = temppass + symbol

    epg=easy_pass_gen(lang)
    #print(epg)
    l = list(temppass)
    random.shuffle(l)
    temppass = ''.join(l)

    l = list(epg)
    random.shuffle(l)
    if rand_num_gen()%2 == 0:
        temppass =  temppass + ''.join(l)
    else:
        temppass = ''.join(l) + temppass
    return temppass
############################################################



def passcheck(passd):
    if len(passd)>4 and len(passd)<20:
        return 1
    else: return 0

def genpass(answer,lang):
    while True:
        if answer == "1":
            passd=easy_pass_gen(lang)
        else:
            passd=strong_pass_gen(lang)
        return passd
        if passcheck(passd)==1:
            return passd
            print("passcheck passed!")
        else:
            print("problem with passcheck")
            genpass(answer,lang)

def main():
    lang = input("EN/GE?")
    answer = input("Do you want a weak or strong password ? (1=weak, 2=strong) : ")
    print(genpass(answer,lang))


if __name__== "__main__":
    main()
