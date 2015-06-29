from django.db.models import Model, CharField, FileField, BooleanField


class Script(Model):
    visible = BooleanField(default=False)
    description = CharField(max_length=150, null=True, blank=True)
    filename = FileField(upload_to='scripts')
    args = CharField(max_length=100, null=True, blank=True)
    interpreter = CharField(max_length=150, default='/bin/bash')

    @property
    def name(self):
        return self.filename.name.split("/")[-1]

    def delete(self, *args, **kwargs):
        storage, path = self.filename.storage, self.filename.path
        super(Script, self).delete(*args, **kwargs)
        storage.delete(path)

    def __str__(self):
        return u'%s' % self.name
