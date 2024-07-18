#1 List is always ordered
#2 A list is changeable
#3 A list allows duplicates
#4 len will help to count the number of items in the list

favouriteMovies = ["John wick, 3Idiots, 12thfail, Dr.strange"]
midtermGrades = [85, 90, 78, 68, 98, 78]
combinedlist = ["John wick, 3Idiots, 12thfail, Dr.strange", 85, 90, 78, 68, 98, 78]
print(combinedlist)

#2
midtermGrades[3]=100
print(midtermGrades)

#4
print(len(midtermGrades))