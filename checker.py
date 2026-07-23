import aiohttp


async def check_username(username):

    username = username.replace("@", "")

    url = f"https://t.me/{username}"


    headers = {
        "User-Agent": "Mozilla/5.0"
    }


    try:
        async with aiohttp.ClientSession(
            headers=headers
        ) as session:

            async with session.get(
                url,
                timeout=10
            ) as response:

                html = await response.text()


                # свободный username
                if "If you have Telegram" in html:
                    return True


                # занят
                if "tgme_page_title" in html:
                    return False


                return False


    except Exception:
        return False
