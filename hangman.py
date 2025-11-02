import random as r
#If you couldn't already tell, this was written by me, jank and all.
#janky hack m8
with open("WordList.csv","r") as f:
    wordlist=[]
    line = f.readline().strip().split(",")
    while line!=[""]:
        for word in line:
            word=word.strip(" ").upper()
            wordlist.append(word)
            
        line=f.readline().strip().split(",")
#wordlist now has every word.

#CHEWS WURD
chosen_word = wordlist[r.randint(0,len(wordlist)-1)]
#print(f"psst secret word is {chosen_word}")


def guess(letters_left):
    guess=""
    notValid=True
    while notValid:
        guess = input("Input letter >>").upper().strip()
        if guess not in letters_left:
            print("Not a valid letter!")
            guess=""
        else:
            print("Valid guess.")
            notValid=False
    return guess

def remove_letter(letter,letters_left):
    for i in range(0,len(letters_left)-1):
        if letters_left[i]==letter:
            letters_left.pop(i)
    return letters_left

def validate(letter,secret_word):
    
    isCorrect=False
    for letterino in secret_word:
        if letterino == letter:
            isCorrect=True
    return isCorrect

def render(correct_letters,chosen_word):
    output=""
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for letter in chosen_word:
        if letter in alphabet:
            empty = True
            for current_letter in correct_letters:
                if letter == current_letter:
                    output += letter
                    empty = False
            if empty:
                output+="_"
        else:
            if letter == " ":
                output+= "  " #done for readability.
            output+=letter
    #print(output)
    return output

def wincheck(ooo,aaa):
    if len(ooo) == len(aaa):
        return True
'''if __name__ == "__main__":    (This would be running it in terminal.)
    win = False                  (No longer needed, so I commented it out, just so it wouldn't run by accident.)
    lives = 10
    guessed = False
    current_full = ""
    letters_left=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    while lives>0 and not(guessed):
        print(f"---------------------------------\n You have {lives} lives remaining.")
        input_letter = guess(letters_left)
        remove_letter(input_letter)
        isCorrect = validate(input_letter)
        if isCorrect:
            current_full+=input_letter
        else:
            print("WRONG!")
            lives-=1
        render(current_full)
        if wincheck(current_full,chosen_word):
            print("winga")
            lives = 0
            win = True
    if win==False:
        print("losega")
        print(f"The word was {chosen_word}")
''' 