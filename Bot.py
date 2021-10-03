from telegram import Update
from telegram.ext import CallbackContext
from datetime import datetime

import auth
import vk


class Bot:

    def __init__(self):
        self.vk_session = auth.auth()

    def get_posts(self, update: Update, context: CallbackContext) -> None:
        try:
            post_count = str(context.args[0])
        except IndexError:
            post_count = "1"

        posts = vk.get_posts(self.vk_session, post_count)

        for post in posts:
            dt_object = datetime.fromtimestamp(post['date'])
            update.message.reply_text(str(dt_object) + "\n" + post['text'])
