from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site


def run():
    print('running seed...')

    clear_data()

    # Change site domain and name.
    # Remember to change it via admin in each one of your application environments.
    site = Site.objects.get_current()
    site.domain = 'localhost:8000'
    site.name = 'Site Name'
    site.save()

    # user
    get_user_model().objects.create_user(
        email='user@capyba.com',
        password='user123?',
        name='Usuário de Teste',
    )
    get_user_model().objects.create_superuser(
        email='admin@capyba.com',
        password='admin123?',
        name='Admin'
    )

    print('seed completed.')


def clear_data():
    # user
    get_user_model().objects.all().delete()
