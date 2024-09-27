from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

# Get all installed apps
app_configs = apps.get_app_configs()

for app_config in app_configs:
    # Loop through all models in each app
    for model_name, model in app_config.models.items():
        try:
            if model_name in ['user','customer','entry','crop','unit','cropcondition','cropcategory','insurance','section','setting','payhistory']:
              # admin.site.register(model)
                @admin.register(model)
                class modelAdmin(admin.ModelAdmin):
                    list_display = [field.name for field in model._meta.fields if field.name != "id"]

                    class Meta:
                        model = model
        except AlreadyRegistered:
            # If the model is already registered, skip it
            pass
