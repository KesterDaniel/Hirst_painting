# Hirst painting
import colorgram


colors = colorgram.extract("image.jpg", 30)


for color in colors:
    new_color = color.rgb
    red = new_color.r
    green = new_color.g
    blue = new_color.b

    color_list.append((red, green, blue))


print(color_list)
