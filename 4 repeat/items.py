exmaple_dictionary = {
    "키A" : "값A",
    "키B" : "값B",
    "키C" : "값C"
}

print("items():", exmaple_dictionary.items())
print()

for key, ele in exmaple_dictionary.items():
    print("dictionary[{}] = {}".format(key, ele))