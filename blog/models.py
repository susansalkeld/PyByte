from django.db import models
import re

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=60)
    summary = models.TextField(max_length=100)
    summary_html = models.TextField(editable=False)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    body_html = models.TextField(editable=False)
    
    class Meta:
        #db_table = 'blog_entries'
        verbose_name_plural = 'entries'
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'

    def __unicode__(self):
        return self.title
    
    
    def get_html_body(self):
        lines = self.body.split('\n')
        #replace with regular expression between <code>/n</code>
        #with 	<section class="box info"><code>>> aslkfdj \n</code></section>

        arrowed_body = ['>>> '+ line for line in lines]
        return self.body #'<br/>'.join(arrowed_body)
    
    def save(self):
        self.body_html = self.get_html_body()
        super(Entry, self).save()
