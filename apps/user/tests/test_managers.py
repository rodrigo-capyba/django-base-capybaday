import pytest

from apps.user.models import User


@pytest.mark.django_db
class TestUserManager:
    """Test UserManager"""

    def test_create_user(self, faker):
        user = User.objects.create_user(faker.email(), None)
        assert not user.is_staff
        assert not user.is_superuser

    @pytest.mark.xfail(raises=ValueError)
    def test_create_user_null_email(self):
        User.objects.create_user(None, None)

    def test_create_superuser(self, faker):
        user = User.objects.create_superuser(faker.email(), None)
        assert user.is_staff
        assert user.is_superuser

    @pytest.mark.xfail(raises=ValueError)
    def test_create_superuser_not_staff(self, faker):
        User.objects.create_superuser(faker.email(), None, is_staff=False)

    @pytest.mark.xfail(raises=ValueError)
    def test_create_superuser_not_super(self, faker):
        User.objects.create_superuser(faker.email(), None, is_superuser=False)
