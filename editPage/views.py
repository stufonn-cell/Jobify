from django.shortcuts import render, redirect, HttpResponse
from django.core.files.base import ContentFile
from plantilla.views import Template
from plantilla.models import TemplateModel
from django.core.paginator import Paginator
from history.models import Vacancy_History
from .models import Avatar
from PIL import Image
import io
import base64

# Create your views here.

# Template object clone


def template_to_edit(request):

   
    if TemplateModel.objects.exists():
        savedTemplate = TemplateModel.objects.latest('id')
        default_name = savedTemplate.name
        
        
        default_brand_logo = savedTemplate.brand_logo
        if 'title' in request.session:
            default_title = request.session['title']
        else:
            default_title = savedTemplate.title
        if 'desc' in request.session:
            default_desc = request.session['desc']
        else:
            default_desc = savedTemplate.desc
        if 'city' in request.session:
            default_city = request.session['city'] 
        else:
            default_city= savedTemplate.city      
        
        if 'color' in request.session:
            default_color = request.session['color']
        else:
            default_color = savedTemplate.color
        
        if 'font' in request.session:
            default_font = request.session['font']
        else:
            default_font = savedTemplate.font
        if 'font_color' in request.session:
            default_font_color = request.session['font_color']
        else:
            default_font_color = savedTemplate.font_color

    baseTemplate = Template(default_name,default_title,default_desc,default_city,default_color, default_font, default_font_color, default_brand_logo)
    return baseTemplate.clone()
    
def step1(request):
    context = {}
    
    queryset_paginator =   Paginator(Avatar.objects.all(), 1)
    page_number = request.GET.get('page')
    page_obj = queryset_paginator.get_page(page_number)
    context['page_obj'] = page_obj
    request.session['page_number'] = page_obj.number

    if 'font' in request.session:
        del request.session['font']
    if 'font_color' in request.session:
        del request.session['font_color']
    if 'color' in request.session:
        del request.session['color']

        
    template = template_to_edit(request)
    context['template'] = template 

    if (request.method == 'POST'):

        title = request.POST.get("title", "").strip()
        desc = request.POST.get("desc", "").strip()
        city = request.POST.get("city", "").strip()
  
        if title and desc and city:
            request.session['title'] = title
            request.session['desc'] = desc
            request.session['city'] = city
            return redirect('paso2/')

    

    context['current_step'] = 1
    context['step_text'] = 'Información básica'
    context['template'] = template
    return render(request, 'step1.html', context)

def step2(request):
    
    template = template_to_edit(request)
 
    context = {}

    queryset_paginator = Paginator(Avatar.objects.all(), 1)
    page_number = request.session.get('page_number', 1)
    page_obj = queryset_paginator.get_page(page_number)
    context['page_obj'] = page_obj

    context['current_step'] = 2
    context['step_text'] = 'Personalización'
    context['template'] = template

    

    if request.method == 'POST':
        if 'change-font' in request.POST:

            font = request.POST['change-font']
  
            template.font = font
            context['template'] = template
            context['page_obj'] = page_obj
            request.session['font'] = font
            return render(request, 'step2.html', context)
        
        if 'change-font-color' in request.POST:

            font_color = request.POST['change-font-color']
            template.font_color = font_color
            context['template'] = template
            context['page_obj'] = page_obj
            request.session['font_color'] = font_color
            return render(request, 'step2.html', context)
        
        if 'change-color' in request.POST:
            color = request.POST['change-color']
            template.color = color
            context['template'] = template
            context['page_obj'] = page_obj
            request.session['color'] = color
            return render(request, 'step2.html', context)
        
        

    context['template'] = template
    return render(request, 'step2.html', context)

def step3(request):
    template = template_to_edit(request)

    if request.method == 'POST':

        if 'imgData' in request.POST and isinstance(request.POST['imgData'], str):
            data_url = request.POST['imgData']
            # Separar correctamente el formato y el contenido base64
            format, imgstr = data_url.split(';base64,')
            # Decodificar la imagen base64 a bytes
            image_data = base64.b64decode(imgstr)
            
            # Crear la imagen desde los bytes
            image = Image.open(io.BytesIO(image_data))
            response = HttpResponse(content_type="image/png")
            image.save(response, "PNG")
            response['Content-Disposition'] = f'attachment; filename="{template.title}.png"'
            if response:
                template_obj_instance = TemplateModel.objects.latest('id')  # Uso correcto de 'id'
                new_history = Vacancy_History()
                new_history.template = template_obj_instance
                new_history.vacancy_image.save(f"{template.title}.png", ContentFile(image_data))
                new_history.save()
            return response

    
    context = {}

    queryset_paginator = Paginator(Avatar.objects.all(), 1)
    page_number = request.session.get('page_number', 1)
    page_obj = queryset_paginator.get_page(page_number)
    context['page_obj'] = page_obj 
    context['current_step'] = 3
    context['step_text'] = 'Descarga tu Vacante'
    context['template'] = template

    return render(request, 'step3.html', context)
