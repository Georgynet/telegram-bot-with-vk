#!/usr/bin/env python
# pylint: disable=C0116,W0613

import logging

import config

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
from Bot import Bot

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def main() -> None:
    updater = Updater(config.token)

    dispatcher = updater.dispatcher

    bot = Bot()

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("getposts", bot.get_posts))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
