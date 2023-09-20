# add to all model classes:
timestamp = models.DateTimeField(auto_now_add=True)
updated = models.DateTime(auto_now=True)

# allows us to shut down this model:
is_active = models.BooleanField(default = True)
