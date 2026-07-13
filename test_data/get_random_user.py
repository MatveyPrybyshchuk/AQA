from faker import Faker


def get_random_user():
    return Faker().name(), Faker().email(), Faker().password(),
