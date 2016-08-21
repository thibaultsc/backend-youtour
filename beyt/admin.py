from django.contrib import admin

from .models import Tour, TranslateTour, Activity, Variation, TourActivity, Location

admin.site.register(Tour)
admin.site.register(TranslateTour)
admin.site.register(Activity)
admin.site.register(Variation)
admin.site.register(TourActivity)
admin.site.register(Location)