import vk_api
from getpass import getpass


def auth_handler():
    remember_device = True
    return input("Enter authentication code: "), remember_device


def auth():
    login, password = input("Enter login: "), getpass()
    vk_session = vk_api.VkApi(
        login, password,
        auth_handler=auth_handler
    )

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    return vk_session
