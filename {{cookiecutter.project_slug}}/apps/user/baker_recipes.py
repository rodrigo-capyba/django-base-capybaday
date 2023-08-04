from faker import Faker
from model_bakery.recipe import Recipe

fake = Faker()

user = Recipe('user.User', email=fake.free_email, name=fake.name)
