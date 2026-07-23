import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

from config import BOT_TOKEN
from checker import check_username


logging.basicConfig(
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🔥 Username Checker Bot\n\n"
        "Проверка Telegram юзернеймов\n\n"
        "Использование:\n"
        "/check username1 username2 username3\n\n"
        "Пример:\n"
        "/check quant glyphix reasonloop"
    )


async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text(
            "❌ Укажи юзернеймы\n\n"
            "Пример:\n"
            "/check quant glyphix"
        )
        return


    usernames = context.args


    msg = await update.message.reply_text(
        "🔎 Проверяю..."
    )


    result = []


    for username in usernames:

        username = username.replace("@", "")

        status = await check_username(username)


        if status:
            result.append(
                f"✅ @{username} — свободен"
            )
        else:
            result.append(
                f"❌ @{username} — занят"
            )


    await msg.edit_text(
        "🔥 Результат:\n\n" +
        "\n".join(result)
    )



def main():

    app = Application.builder() \
        .token(BOT_TOKEN) \
        .build()


    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CommandHandler("check", check)
    )


    print("Bot started")

    app.run_polling()



if __name__ == "__main__":
    main()
