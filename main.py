print("Fill-in the blank Lyrics!")
print("type in the blank lyrics,see if you're as cool as me")
i = 1

while True:
  color = input("Never going to ____ you up\n")
  if color == "give":
    break
  else:
    i += 1
    print("Nope, try again")
print("Well done, it only took you", i, "attempts!")