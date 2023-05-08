import asyncio
import telegram


async def main():
    bot = telegram.Bot("5700293363:AAEvN9JLGvpbkAYXL5zNtPQWn_AKHNTBI5o")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())