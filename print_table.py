table_data = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]


def print_table(table):
    col_w = [0] * len(table)
    for i in range(len(table)):
        for k in table[i]:
            if col_w[i] < len(k):
                col_w[i] = len(k)
    print(col_w)
    for x in range(len(table[0])):
        for y in range(len(table)):
            print(f"{table[y][x].rjust(col_w[y]+1)}", end="")
        print()


print(print_table(table_data))
