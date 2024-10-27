from rest_framework import viewsets, exceptions, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .serializers import (PostSerializer,
                          GroupSerializer,
                          CommentSerializer,
                          FollowSerializer)

from posts.models import Post, Group, Follow
from .permissions import IsAuthorOrReadOnlyPermission
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise exceptions.NotAuthenticated(
                'Неавторизованный пользователь не может создать пост.')
        serializer.save(author=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):

    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    permission_classes = [IsAuthenticated]
    search_fields = ('following__username',)
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(user=user)

    def perform_create(self, serializer):
        following_username = serializer.validated_data['following']
        try:
            following_user = User.objects.get(username=following_username)
        except User.DoesNotExist:
            raise exceptions.ValidationError('Пользователь не найден.')

        if following_user == self.request.user:
            raise exceptions.ValidationError(
                'Вы не можете подписаться на себя.')

        if Follow.objects.filter(
                user=self.request.user, following=following_user).exists():
            raise exceptions.ValidationError(
                'Вы уже подписаны на этого пользователя.')

        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthorOrReadOnlyPermission,)
    serializer_class = CommentSerializer

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        post = self.get_post()
        return post.comments.all()

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise exceptions.NotAuthenticated(
                'Неавторизованный пользователь не может создать комментарий.')
        post = self.get_post()
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
