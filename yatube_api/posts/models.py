from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

MAX_STR_LENGTH = 30


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="Слаг")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        default_related_name = "groups"

    def __str__(self):
        return self.title[:MAX_STR_LENGTH]


class Post(models.Model):
    text = models.TextField(verbose_name="Текст")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор",
    )
    image = models.ImageField(
        upload_to="posts/",
        null=True,
        blank=True,
        verbose_name="Изображение",
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True,
        verbose_name="Группа",
    )

    class Meta:
        default_related_name = "posts"

    def __str__(self):
        return self.text[:MAX_STR_LENGTH]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Автор",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Пост",
    )
    text = models.TextField(verbose_name="Текст")
    created = models.DateTimeField(
        "Дата добавления",
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        default_related_name = "comments"

    def __str__(self):
        return f"{self.author.username[:15]}: " f"{self.text[:MAX_STR_LENGTH]}"
