### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
  # missing def __init__(self):

  def check_for_ace(self, card):
    if card.value = 1: 
      # should be ==
      return True
    else
    # missing colon after else
      return False
   

  dif highest_card(self, card1 card2): 
  # def not dif, and need a comma to seperate the two card parameters
  #whole section below has incorrect indentation
  if card1.value > card2.value:
    return card 
    # should be return card1
  else:
    return card2
  


def cards_total(self, cards):
#indentation error needs to be indented into the class
  total
  # need to define what total is e.g. total = 0 for as a start point
  for card in cards:
    total += card.value
    return "You have a total of" + total
    # total will be an int and cannot be concatenated like this.
    # try f"You have a total of {total}."
  
```
