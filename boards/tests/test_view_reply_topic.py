from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Board, Topic, Post
from ..views import reply_topic


class ReplyTopicTestCase(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='this board is dedicated for django discussion')
        self.username = 'john'
        self.password = '12345@john'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        self.topic = Topic.objects.create(subject='User Cred.', board=self.board, starter=user)
        Post.objects.create(message='LJLSJDF ERJLERJ sferj', topic=self.topic, created_by=user)
        self.url = reverse('reply_topic', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk})
