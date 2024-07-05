from django.contrib import admin
from .models import DiabetesInput

class DiabetesAdmin(admin.ModelAdmin):
    list_display = ('glucose','blood_pressure','bmi','insulin','skinthickness','pregnancies','Age','DiabetesPedigree','Prediction')

admin.site.register(DiabetesInput, DiabetesAdmin)



# Register your models here.
