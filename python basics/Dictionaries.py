phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
phonebook["Jake"] = 938273443
del phonebook["Jill"]

if "Jake" in phonebook:
    print("Jake was added to the phonebook.")
    # add Jake

if "Jill" not in phonebook:
    print("Jill was removed from the phonebook.")
    #remove Jill
