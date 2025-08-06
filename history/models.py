from django.db import models
from plantilla.models import TemplateModel
from django.utils import timezone

class Vacancy_History(models.Model):
    template = models.ForeignKey(TemplateModel, null=False, default=1, on_delete=models.CASCADE)
    vacancy_image = models.ImageField(null=False, upload_to="vacancies/")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Vacancy History {self.id} for Template {self.template.id}"



