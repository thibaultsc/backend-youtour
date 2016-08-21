from django.contrib import admin

from .models import Tour, Activity, Variation, TourActivity

admin.site.register(Tour)
admin.site.register(Activity)
admin.site.register(Variation)
admin.site.register(TourActivity)