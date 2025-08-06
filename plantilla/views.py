from django.shortcuts import render
import copy

# Create your views here.

def plantilla(request):

    return render(request, 'plantilla.html')

class Template:
    def __init__(self, name, title,description, city, color, font, font_color, brand_logo):
        self.name = name
        self.title = title
        self.desc = description
        self.city = city
        self.color = color
        self.font = font
        self.font_color = font_color
        self.brand_logo = brand_logo


    def clone(self):
        return copy.deepcopy(self)



