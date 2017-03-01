def multiples(x):
    #to check if the input is number or not
    #the normal if else condition cannot handle large inputs
    try:
        if x <= 0:
            return 0
        x = int(x) - 1

        #sum of n numbers formula is (n*n+1)/2

        sum_of_3 = ((x/3) * ((x/3)+1)) // 2 #sum of numbers that are divided by 3
        sum_of_5 = ((x/5) * ((x/5)+1)) // 2 #sum of numbers that are divided by 15
        sum_of_15 = ((x/15) * ((x/15)+1)) // 2 #sum of numbers that are divided by 15
        # we subtract the sum of 15 because it gets added twice
        # multiply the sum with their respective numbers to get mulitples of each number

        final_sum = sum_of_3*3 + sum_of_5*5 - sum_of_15*15 

        return final_sum
    except ValueError:
        return "Enter a valid number!"


#print multiples(-56321)
#print multiples("anurag")
