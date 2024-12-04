def improve_password(input_dictionary, string):

  new_string = ""

  for keywords in string:
    if keywords in input_dictionary:
        new_string += input_dictionary[keywords]
    else:
        new_string += keywords
  return new_string

improvements = {
  's': '$',
  'S': '$',
  'A': '4',
  'a': '@',
  'e': '3',
  'B': '8',
}

print(improve_password(improvements, 'sSAeJAIDENB'))



  

  