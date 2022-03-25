from background_task import background

from main.models import Post

DAILY = 60 * 60 * 24


@background()
def reset_upvotes():
    Post.objects.update(upvotes=0)


reset_upvotes(repeat=DAILY)
