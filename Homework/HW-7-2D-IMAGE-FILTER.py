from PIL import Image
from image_converter import list_to_image, image_to_list
import copy

# An example function provided for you that darkens an image.

def darken(pixels):

  new_pixels = copy.deepcopy(pixels)
  for row in range(len(pixels)):
    for col in range(len(pixels[row])):
      r = new_pixels[row][col][0]
      g = new_pixels[row][col][1]
      b = new_pixels[row][col][2]
      new_pixels[row][col] = [r / 2, g / 2, b / 2]
  return new_pixels


# DEFINE YOUR FUNCTIONS HERE.
def red_stripes(pixels):
  new_pixels = copy.deepcopy(pixels)
  length = len(pixels)
  for row in range(length):
    for column in range(0,len(pixels[row]),100):
      new_column = 0
      while new_column < 50 and column < len(pixels[row]):
       new_pixels[row][column] = [255,0,0]
       column = column + 1
       new_column = new_column + 1
  return new_pixels


def border(pixels, list): 
  new_pixels = copy.deepcopy(pixels)
  length = len(pixels)
  row = 0


  for row in range(0,30):
     for column in range(0,len(pixels[row])):
      new_pixels[row][column] = list
    
  for row in range(30,(length-30)):
    column = 0
    

    for column in range(0,30):
        new_pixels[row][column] = list
      
    for column in range(len(pixels[row])-30, len(pixels[row])):
        new_pixels[row][column] = list

  for row in range((length-30),length):
      for column in range(0,len(pixels[row])):
         new_pixels[row][column] = list
 
  return new_pixels

            
def rotate_180(pixels):
     
    new_pixels = copy.deepcopy(pixels)
    length = len(new_pixels)
    new_list = []
    for x in range(-1, -length-1, -1):
      element = new_pixels[x]
      new_list.append(element)


    final_list = []

    for y in range(length):
      new_list_2 = []
      for z in range(-1, -len(new_list[y])-1, -1):
        element = new_list[y][z]
        new_list_2.append(element)

      final_list.append(new_list_2)

    return final_list
           

# Open an image

# pb_img = Image.open("fisk_gate.png")

# pixels = image_to_list(pb_img)



# CALL YOUR FUNCTION HERE TO TEST IT OUT.

# changed_pixels = darken(pixels)

# changed_pixels_2 = red_stripes(pixels)

# changed_pixels_3 = border(pixels, [0,255,0])

# changed_pixels_4 = rotate_180(pixels)

# Save an image

# new_pb_img = list_to_image(changed_pixels)

# new_pb_img.save("fisk_gate_new.png")