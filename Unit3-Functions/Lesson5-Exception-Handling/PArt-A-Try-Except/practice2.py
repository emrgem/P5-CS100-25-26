def join_study_squad(members):
    if members == "":
        print("Squad disbanded :(")
        return 0
    count = 1 # at least one member
    found_non_separator = False
    for char in members:
        if char == ",":
            count += 1
        else:
            found_non_separator = True
    
    if not found_non_separator: #if string only contains commas
        print("Squad disbanded :(")
        return 0
    return count
print(join_study_squad("Alice,Bob,Charlie"))
print(join_study_squad(",,,"))
print(join_study_squad(""))
print(join_study_squad("Solo Student") )