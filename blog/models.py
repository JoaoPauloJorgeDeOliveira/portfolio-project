from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100] + '...'

    def pub_date_pretty(self):
        return self.pub_date.strftime('%d/%m/%Y')

    def __str__(self):  # Now, in admin page, blog title displays 'tile'
        return self.title
