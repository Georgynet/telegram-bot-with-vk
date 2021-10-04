import config


def get_posts(vk_session, max_posts) -> list:
    vk = vk_session.get_api()
    wall = vk.wall.get(count=max_posts, owner_id=config.wall_id)

    return wall['items']
