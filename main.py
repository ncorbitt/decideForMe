from random import randint
"""
Juggling multiple programming languages like Python, JavaScript, C++, SQL, and Bash can 
be overwhelming. I often find myself diving deep into one language, only to neglect others.
To maintain a balanced learning pace, I created this small program that randomly picks 
which language to focus on each day of the week. This ensures consistent progress across 
all languages.

"""

def main():
  newlist = []
  weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

  # # List of things
  list = ['python', 'c++', 'bash', 'javascript', 'SQL']

  while range(len(list)):
    # get random number
    rnum = randint(0, len(list) - 1)
    # Pick a random item from the list of things, removing it from the list
    item = list.pop(rnum)
    # Build new list
    newlist.append(item)

  # Field Width
  fieldWidth = 12
  # Print weekdays
  for i in range(0, len(weekday)):
    print(f'{weekday[i].upper():{fieldWidth}}', end=' ')
  print()  # Print a new line

  # print dashes under weeekdays
  for i in range(0, len(weekday)):
    print(f"{'-'*len(weekday[i]):{fieldWidth}}", end=' ')
  print()  # Print a new line

  # Print the list
  for i in range(0, len(weekday)):
    try:
      print(f"{newlist[i].upper():{fieldWidth}}", end=' ')
    except IndexError:
      print(f"{'N/A':{fieldWidth}}", end=' ')
  print()  # Print a new line


if __name__ == '__main__':
  main()
