favouriteMovies = ["John wick", "3Idiots", "12thfail", "Dr.strange"]
for everyitem in favouriteMovies :
    print(everyitem)    #print without string


sentence = ""
for everyitem in favouriteMovies :    
    sentence = sentence + everyitem + " "    #(shortcut method) sentence += everyitem + " " 
print(sentence)
