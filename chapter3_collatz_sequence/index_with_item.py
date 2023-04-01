things = ["koka", True, 554, "bola"]
for i in range(
    len(things)
):  # if you want item with index this is one method to do that
    print(f"Index: {i} containt item: {things[i]}")


# another method
for index, item in enumerate(things):
    print(f"Index: {index} containt item: {item}")

new_things = things[:]
things[1] = False
print(things)
print(new_things)
print(id(things))
print(id(new_things))
