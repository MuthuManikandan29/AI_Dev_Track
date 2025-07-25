# Task 3: Favorite Movies List
# Ask the user how many favorite movies they want to enter.
#
# Store those in a list using a loop.
#
# Print the full list at the end.

num=int(input("enter how many movies you want to enter : "))
fav_movies=[]
for i in range(num):
    movie=input(f"enter your fav movie #{i+1} :")
    fav_movies.append(movie)
print("\nyour fav movies list ")
for movie in fav_movies:
    print(f"-{movie}")