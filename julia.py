# This script generates an image of the Julia set
#   without importing image manipulation libraries.

def f(z,c):
  """Given complex values z and c, outputs a number indicating the speed of divergence"""
  n = 1
  while n<256 and abs(z)<=10:
    z, n = z*z+c, n+1
  return n-1

def palette(n):
  """Given a number n between 0 and 255, outputs RGB values along a predefined gradient"""
  return bytes([max(abs(210-n),0),max(abs(85-n),0),max(abs(30-n),0)])

# BMP file header specifying that the dimensions are 512*512 pixels
header = b'BM' + bytes([0]*8 + [54, 0, 0, 0] + [40, 0, 0, 0] + [0, 4, 0, 0]*2 + [1, 0, 24] + [0]*25)  

# Open the file for writing
with open('julia.bmp','wb+') as julia:
  
  julia.write(header)

  c = -0.7 + 0.3j

  # Iterate over the pixels, calculate the speed of divergence, and paint the corresponding color
  for y in range(-512,512):
    for x in range(-512,512):
      z     = x/512 + y/512 * 1j
      color = f(z, c)
      julia.write(palette(color))