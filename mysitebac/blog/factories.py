from django.contrib.auth.models import User
from django.utils.timezone import now

import factory
from faker import Factory as FakerFactory

from blog.models import Post

faker = FakerFactory.create()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda x: faker.name())
    email = factory.Faker('email')
    
    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user
    
class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.LazyAttribute(lambda x: faker.sentence())
    author = factory.SubFactory(UserFactory)
    created_on = factory.LazyFunction(lambda x: now())
    status = 0

    class Meta:
        model = Post