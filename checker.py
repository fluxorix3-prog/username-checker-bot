import aiohttp


async def check_username(username):

    url = f"https://t.me/{username}"


    try:

        async with aiohttp.ClientSession() as session:

            async with session.get(
                url,
                timeout=10
            ) as response:


                text = await response.text()


                if "If you have Telegram" in text:
                    return True


                return False


    except Exception:

        return False
