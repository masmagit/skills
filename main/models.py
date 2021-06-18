from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, related_name='skills')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class JobPosting(models.Model):
    LEVEL = (
        ('l', 'Lead'),
        ('s', 'Senior'),
        ('m', 'Mid-level'),
        ('j', 'Junior'),
    )

    TYPE = (
        ('f', 'Full time'),
        ('c', 'Contract'),
    )

    REMOTE = (
        ('y', 'Yes'),
        ('p', 'Partial'),
        ('n', 'Not specified'),
    )
  
    title = models.CharField(max_length=200)
    date = models.DateField()
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, related_name='jobposts')
    level = models.CharField(max_length=1, choices=LEVEL, blank=True)
    type= models.CharField(max_length=1, choices=TYPE, blank=True)
    remote = models.CharField(max_length=1, choices=REMOTE, default='n', blank=True)
    content = models.TextField(blank=True)
    url = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill, related_name='jobposts')
    main_skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True, blank=True, related_name='main_skill_jobposts')

    class Meta:
        unique_together = ('title', 'company',)

    def __str__(self):
        return self.title

class Company(models.Model):
    SIZE = (
        ('u', 'Unknown'),
        ('1', '1-10'),
        ('2', '11-50'),
        ('3', '51-200'),
        ('4', '201-500'),
        ('5', '500+'),
    )

    name = models.CharField(max_length=100)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, blank=True, related_name='companies')
    industry = models.ForeignKey('Industry', on_delete=models.SET_NULL, null=True, blank=True, related_name='companies')
    size = models.CharField(max_length=1, choices=SIZE, default='u')

    class Meta:
        unique_together = ('name', 'country',)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=80)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True, blank=True, related_name='countries')

    def __str__(self):
        return self.name

class Industry(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name
