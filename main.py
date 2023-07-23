from sketchpy import library as lib

#first inbuilt image
#first=lib.rdj()                       # JUST REMOVE COMMENTS TO USE THE CODE
#first.draw()

# Second inbuilt image
# new = lib.flag()
# new.draw()

# Third inbuilt image
#obj = lib.bts()
#obj.draw()

# Raw image into sketch
from sketchpy import canvas
raw = canvas.sketch_from_image("doraemon.jpg")
raw.draw()
