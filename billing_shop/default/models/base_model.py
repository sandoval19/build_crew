from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.CharField(primary_key=True, unique=True, null=False, default='Empty', editable=False, max_length=255)
    is_active = models.BooleanField('State', default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.id = str(uuid.uuid4())
        super().save(*args, **kwargs)
    
    class Meta:
        abstract = True
