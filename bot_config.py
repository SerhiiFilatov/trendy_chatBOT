from environs import Env
from dataclasses import dataclass



@dataclass
class Bots:
    bot_token: str
    admin_id: list[int]



@dataclass
class Settings:
    bots: Bots


def get_config(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots = Bots(
            bot_token=env.str('BOT_TOKEN'),
            admin_id=list(map(int, env.list('ADMIN_ID'))),
        )
    )

settings = get_config('.env')



