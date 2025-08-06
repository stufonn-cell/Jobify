from django.shortcuts import render
from history.models import Vacancy_History
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def history_view(request):
    context = {}
    history = Vacancy_History.objects.all()
    context['history'] = history

    if request.method == 'POST':
        if 'download' in request.POST:
            vacancy_to_download = get_object_or_404(Vacancy_History, pk=request.POST['download'])
            response = HttpResponse(vacancy_to_download.vacancy_image, content_type='image/png')
            response['Content-Disposition'] = f'attachment; filename="{vacancy_to_download.template.name}.png"'
            return response
        
        if 'delete' in request.POST:
            vacancy_to_delete = get_object_or_404(Vacancy_History, pk=request.POST['delete'])
            vacancy_to_delete.delete()

    return render(request, 'history_page.html', context)
