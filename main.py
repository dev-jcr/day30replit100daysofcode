# f-strings
print("30 Days Down")
for i in range(1, 31):
  print(f"\n\nDay {i}")
  print(f"What did you though of the day {i}?")
  thought = input()
  # response = f"\nYou thought Day {i: ^}"
  myText = f"You thought day {i} was "
  print(f"{myText:^35}")
  print(f"{thought:^35}")
  print()