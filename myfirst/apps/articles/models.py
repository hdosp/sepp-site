import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
	article_title = models.CharField('название статьи', max_length = 200)
	article_text = models.TextField('текст статьи')
	article_short = models.CharField('краткое описание', max_length = 50)
	pub_date = models.DateTimeField('дата публикации')

	def __str__(self):
		return (self.article_title) + " - " + (self.article_short)

	def was_pub_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 1))

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField('имя автора', max_length = 50)
	comment_text = models.CharField('текст комментария', max_length = 200)
	comment_pub = models.DateTimeField('дата публикации')

	def __str__(self):
		return self.author_name

	def was_pub_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(hours = 2))

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'
