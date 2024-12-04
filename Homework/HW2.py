isRed = True
isWhite = True
isBlue = False
if not isRed or not isWhite or not isBlue:
  print('sugar')
  if isBlue or isRed:
    print('spice')
#Here two "if's" are used, so the program checks every "if" even if the condition of one "if" is fulfilled. However, if we use elif/else, the program ends immediately
if not not (not (isBlue and isRed) or isWhite):
  print('flour')
elif isRed:
  print('salt')
else:
  print('pepper')
