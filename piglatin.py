import re
import string

#this function is used to split words that contains alphabets,numbers,symbols
def split_numbers(letters):
    #temp list to store each character
    l = []
    for i in letters:
        #appends each character to list l
        l.append(i)
    #if len=2 it adds ay to the end of alphabet
    if len(l) <= 2:
        for i in range(len(l)):
            if l[i].isalpha():
                l[i] = l[i]+"ay"
        return "".join(l)


    for i in range(len(l)):
        #checks if character is alpha adds to temp variable and remove it and break in the end
        if l[i].isalpha():
            temp = l[i]
            l.remove(l[i])
            #reverse loop to get the first alphabet from reverse and append temp + ay and break
            for j in reversed(range(len(l))):
                if l[j].isalpha():
                    l[j] = l[j] + temp + "ay"
                    break
            break
    #return the join of elements in l
    temp_ans = "".join(l)
    return temp_ans

def piglatin(x):

    # gets each character from the given input and adds a space if character is found to split easily with space delimiter
    each_letter_list = []
    for letter in x:
        if letter in string.punctuation:
            each_letter_list.append(" %s" % letter)
        else:
            each_letter_list.append(letter)
    temp_string = "".join(each_letter_list)

    #temp_list contains the each word split with space delimiter

    temp_list = temp_string.split(" ")

    #loop through each word in temp_list

    for word in range(len(temp_list)):
        #if the word contains characters,numbers and alphabets split_numbers method is called
        if not temp_list[word].isalpha():
            temp_list[word] = split_numbers(temp_list[word])

        #else remove first letter and add it with ay in the end
        else:
            temp_list[word] = temp_list[word][1:] + temp_list[word][0] + "ay"
        #print word
    #return the join of list with space
    ans = " ".join(temp_list)
    #removes extra space before punctutaion in the answer
    ans = re.sub(r'\s+([@$?.!",=+#()])', r'\1', ans)
    return ans
#print piglatin("@#$apple$@ 233anurag3234235 1anurag anurag2 2@anurag anurag2@")
