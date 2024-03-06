from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class LearningTag(models.Model):
    name = models.CharField(max_length=20)

    # Function here will make it show STR Name vs object number in admin view
    def __str__(self):
        return self.name


class Learned(models.Model):
    title = models.CharField(max_length=200)
    tldr = models.CharField(max_length=300)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        Author,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="creating_author",
    )
    modified_by = models.ForeignKey(
        Author,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="modifying_author",
    )
    tags = models.ManyToManyField(LearningTag)

     # Function here will make it show STR Name vs object number in admin view
    def __str__(self):
        return self.title