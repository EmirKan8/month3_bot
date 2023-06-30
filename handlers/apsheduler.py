import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import bot, users
from apscheduler.triggers.date import DateTrigger


async def go_to_sleep(text):
    for user in users:
        await bot.send_message(
            user, f"ИДи спаать {text} !"
        )


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")
    scheduler.add_job(
        go_to_sleep,
        DateTrigger(
            run_date=datetime.datetime(year=2023, month=7, day=1)
        )
    )
    scheduler.start()
