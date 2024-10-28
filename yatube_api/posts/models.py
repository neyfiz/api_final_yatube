from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):

    title = models.CharField(max_length=200, verbose_name='Group Name')
    slug = models.SlugField(unique=True, verbose_name='Unique Identifier')
    description = models.TextField(verbose_name='Group Description')

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return self.title


class Post(models.Model):

    text = models.TextField()
    pub_date = models.DateTimeField('Publication Date', auto_now_add=True)

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Author')

    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Image')

    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name='Group')

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.text[:30]


class Comment(models.Model):

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Author')

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Post')
    text = models.TextField(verbose_name='Comment Text')

    created = models.DateTimeField(
        'Creation Date',
        auto_now_add=True,
        db_index=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text[:30]


class Follow(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='follower',
        verbose_name='Follower')

    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='following',
        verbose_name='Following')

    class Meta:
        verbose_name = 'Follow'
        verbose_name_plural = 'Follows'
        constraints = [
            models.UniqueConstraint(fields=['user', 'following'],
                                    name='unique_user_following')
        ]

    def __str__(self):
        return f"{self.user.username} follows {self.following.username}"
