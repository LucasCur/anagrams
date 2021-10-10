words = ["Xyz","Abc","Aba","Test"]
debounce = "false"
toSolve = input("Anagram to solve: ")
for i in range(len(words)):
  if sorted(words[i].lower()) == sorted(toSolve.lower()):
    print(toSolve,"is an anagram of",words[i])
    debounce = "true"
if debounce == "false":
  print(toSolve,"is not an anagram of any word(s) from the array.")
