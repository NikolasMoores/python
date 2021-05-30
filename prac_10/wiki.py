import wikipedia
search = input("Enter wikipedia search:")
while search != "":
    try:
        print(wikipedia.summary(search))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)

    search = input("Enter wikipedia search:")
