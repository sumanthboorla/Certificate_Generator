### Pillow module

Using the [pillow module](https://pypi.org/project/Pillow/) to make changes.
- Calculating and declaring default values.


```python
from PIL import Image, ImageFont, ImageDraw

'''Global Variables'''
FONT_FILE = ImageFont.truetype(r'font/GreatVibes-Regular.ttf', 180)
FONT_COLOR = "#FFFFFF"

template = Image.open(r'template.png')
WIDTH, HEIGHT = template.size
```

```python
def make_certificates(name):
    '''Function to save certificates as a .png file
    Finding the width and height of the text. 
    Placing it in the center, then making some adjustments.
    Saving the certificates in a different directory.
    '''
    
    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name, font=FONT_FILE)
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_FILE)
    
    image_source.save("./out/" + name +".png")
    print('Saving Certificate of:', name)        

```

