from django.db.models import Model, CharField, FileField, BooleanField


class Script(Model):
    description = CharField(max_length=150, null=True, blank=True)
    visible = BooleanField(default=False)
    filename = FileField(upload_to='scripts')

    @property
    def name(self):
        return self.filename.name.split("/")[-1]
