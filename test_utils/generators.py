from model_mommy import mommy
from model_mommy.random_gen import gen_string


def gen_post_title():
    return f'Post {gen_string(5)}'


mommy.generators.add('django.db.models.fields.CharField', gen_post_title)
