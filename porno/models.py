from django.db import models

class PornCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# models.py veya admin.py içinde

import re
from django.db import models

def extract_external_id_from_url(url):
    """
    Pornhub video URL'sinden embed için gerekli external_id (viewkey) çıkarır.
    Örnek url: https://www.pornhub.com/view_video.php?viewkey=674e82c7d8589
    """
    match = re.search(r'viewkey=([a-zA-Z0-9]+)', url)
    if match:
        return match.group(1)
    return None

class PornVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)  # tüm video linkleri buraya
    external_id = models.CharField(max_length=50, blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(PornCategory, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.video_url and not self.external_id:
            ext_id = extract_external_id_from_url(self.video_url)
            if ext_id:
                self.external_id = ext_id
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title
