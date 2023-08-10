import send2trash

# Professional Way to Do
# with open("bacon.txt", "w") as file:
#     file.write("becon is not vegitable")

becon_file = open("bacon.txt", "a")
becon_file.write("Fuck")
becon_file.close()
send2trash.send2trash("bacon.txt")
