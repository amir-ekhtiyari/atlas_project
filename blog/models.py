from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_resized import ResizedImageField


# ============================
# (posts)    پست ها
# ============================


# Managers
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


# Create your models here.

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        REJECTED = 'RJ', 'Rejected'

    # relations
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')

    # data fields
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField()

    # date
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # Choices field
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['publish']),
        ]

    def __str__(self):
        return self.title


# ============================
# جزییات پست ها (postdetail)
# ============================


# Managers

class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class PostDetail(models.Model):
    class Condition(models.TextChoices):
        NEW = 'NW', 'New'
        USED = 'US', 'Used'
        REFURBISHED = 'RF', 'Refurbished'

    # Relations
    post = models.OneToOneField("Post", on_delete=models.CASCADE, related_name="details")

    # Data fields
    title = models.CharField(max_length=250, verbose_name="عنوان", null=True, blank=True)

    description = models.TextField(verbose_name="توضیحات", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=50, unique=True)  # Stock Keeping Unit
    condition = models.CharField(max_length=2, choices=Condition.choices, default=Condition.NEW)
    is_available = models.BooleanField(default=True)

    # Date
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Managers
    objects = models.Manager()
    available = AvailableManager()

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['sku']),
            models.Index(fields=['-created']),
        ]
        verbose_name = "Post Detail"
        verbose_name_plural = "Post Details"

    def __str__(self):
        return f"{self.title} ({self.post.title}) - {self.sku}"



# ============================
# خدمات (Services)
# ============================
class ServiceManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ServiceManager()

    def __str__(self):
        return self.title


# ============================
# پروژه‌ها (Projects)
# ============================
class ProjectManager(models.Manager):
    def visible(self):
        return self.filter(is_visible=True)


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Website'),
        ('ml', 'Machine Learning'),
        ('app', 'Mobile App'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    url = models.URLField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web')
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ProjectManager()

    def __str__(self):
        return self.title


# ============================
# اعضای تیم
# ============================
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    joined_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# ============================
# مشتریان / برندها
# ============================
class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients/', blank=True, null=True)
    website = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ============================
# درباره ما
# ============================
class About(models.Model):
    heading = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading


# ============================
# تماس با ما
# ============================
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Image(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="تصویر"
    )
    post_detail = models.ForeignKey(
        'PostDetail',
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="تصویر جزییات",
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=250,
        verbose_name="عنوان",
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name="توضیحات",
        null=True,
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True)
    image_field = ResizedImageField(
        size=[800, 600],  # resize to 800x600
        upload_to="post_images/",
        quality=75,  # optional: JPEG quality
        crop=['middle', 'center'],  # optional: crop before resize
        force_format='JPEG'  # optional: force to JPEG
    )

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]
        verbose_name = "تصویر"
        verbose_name_plural = "تصویر ها"

    def __str__(self):
        return self.title if self.title else "none"
