from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    ROLE_CHOICE = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin')
    ]

    role = models.CharField(
        choices=ROLE_CHOICE,
        default=USER,
        max_length=9
    )
    email = models.EmailField(
        verbose_name='email address',
        unique=True,
        max_length=254)
    first_name = models.CharField(
        verbose_name='first name',
        max_length=150,
        blank=True)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return bool(self.role == self.ADMIN)

    @property
    def is_moderator(self):
        return bool(self.role == self.MODERATOR)

    @property
    def is_user(self):
        return bool(self.role == self.USER)


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.CharField(
        max_length=200,
        null=True,
        blank=True)
    genre = models.ManyToManyField(
        'Genre',
        related_name='titles')
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True,
        null=True)

    class Meta:
        ordering = ['year']
        verbose_name = 'Название произведения'
        verbose_name_plural = 'Названия произведений'

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='author',
        null=False)
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True)
    score = models.PositiveIntegerField(
        default=10,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='оценка')
    title = models.ForeignKey(
        'Title',
        blank=True,
        null=True,
        related_name='reviews',
        on_delete=models.SET_NULL)
    text = models.TextField(
        verbose_name='текст оценки',
        help_text='оцените произвидение')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review')
        ]
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        verbose_name='author',
        null=False)
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True)
    review = models.ForeignKey(
        'Review',
        related_name='comments',
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    text = models.TextField(
        verbose_name='текст коментария',
        help_text='добавьте коментарий')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
