
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Article(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    text = models.TextField("Текст")
    created_date = models.DateField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-created_date', 'title']

    def __str__(self) -> str:
        return f"{self.title} ({self.author})"

    def get_excerpt(self) -> str:
        """
        Возвращает первые 140 символов текста.
        Если текст длиннее — добавляет многоточие.
        """
        if not self.text:
            return ""
        excerpt = self.text[:140]
        return excerpt + "..." if len(self.text) > 140 else excerpt

    def get_absolute_url(self):
        """
        Используется для ссылки на детальную страницу статьи.
        """
        return reverse('article_detail', args=[str(self.id)])
