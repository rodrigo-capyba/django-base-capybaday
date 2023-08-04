import pytest
from model_bakery import baker

from django.core import mail
from django.test import TestCase


@pytest.mark.django_db
class TestUser:
    def test_get_full_name(self, faker):
        name = faker.name()
        isntance = baker.make('user.User', name=name)
        assert isntance.get_full_name() == name

    def test_get_short_name(self, faker):
        first_name = faker.first_name_nonbinary()
        last_name = faker.last_name_nonbinary()
        name = f"{first_name} {last_name}"
        instance = baker.make('user.User', name=name)
        assert instance.get_short_name() == first_name

    def test_email_user(self, faker):
        instance = baker.make('user.User')
        title = faker.word()
        message = faker.text()
        from_email = faker.email()
        instance.email_user(title, message, from_email)
        assert len(mail.outbox) == 1
        assert mail.outbox[0].body == message
