def count_characters(s):
    #Initializing an empty dictionary
    count = {}

    #Iterating over contents of what's being passed
    for i in s:
        #If char already in dictionary add 1 to its count
        if i in count:
            count[i] += 1
        #If new char, add to dictionary for first time and set to 1
        else:
            count[i] = 1

    #Print dictionary
    print(count)

#Prompt user for input
word = input("Enter your string:")

#Call function
count_characters(word)