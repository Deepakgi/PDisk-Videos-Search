# (c) @AbirHasan2005

from core.login import droplink_login

droplink_DB = {}


async def get_cookies(username: str, password: str) -> str:
    if not droplink_DB:
        user_id, cookies = await droplink_login(username, password)
        droplink_DB["cookies"] = cookies
        droplink_DB["user_id"] = user_id
        droplink_DB["username"] = username
        droplink_DB["password"] = password

    return droplink_DB["cookies"]


async def set_cookies(data: dict):
    droplink_DB["username"] = data["username"]
    droplink_DB["password"] = data["password"]
    droplink_DB["user_id"] = data["user_id"]
    droplink_DB["cookies"] = data["cookies"]
