# A set is unchangeable just like a tuple but you can remove or add new items.
# A set is unordered 
# A set is not indexed

favouriteMovies = {"John wick", "3Idiots", "12thfail", "Dr.strange"}
midtermGrades = {85, 90, 78, 68, 98, 78}
combinedlist = {"John wick", "3Idiots", "12thfail", "Dr.strange", 85, 90, 78, 68, 98, 78}
print(combinedlist)

combinedlist.remove(90)
combinedlist.add("Spiderman")
print(combinedlist)