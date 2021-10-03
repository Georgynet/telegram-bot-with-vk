import vk_api
import config


def get_posts(vk_session, max_posts):
    tools = vk_api.VkTools(vk_session)
    wall = tools.get_all('wall.get', max_posts, values={'owner_id': config.wall_id})

    return wall['items']
