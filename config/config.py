from environs import Env # https://pypi.org/project/environs/

env = Env()
env.read_env() # read .env file if it exists

db_database = env.str("DB_PATH")
production = env.str("PRODUCTION")

user_home = env("HOME")
