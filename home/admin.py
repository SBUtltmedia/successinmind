from django.contrib import admin

# Register your models here.
from home import models

admin.site.register(models.Profile)

admin.site.register(models.MentalFitnessAssessment)
admin.site.register(models.Confidence)
admin.site.register(models.Concentration)
admin.site.register(models.Challenge)
admin.site.register(models.Composure)
admin.site.register(models.Commitment)

admin.site.register(models.Team_MentalFitnessAssessment)

admin.site.register(models.Journal)
admin.site.register(models.WeeklyPlan)
