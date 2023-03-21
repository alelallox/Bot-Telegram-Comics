import asyncio
import schedule
import time

print("ciaoooooo")
a = "ciao"
async def job(a):
    print(a)


schedule.every(30).seconds.do(lambda: job(a))

while True:
    schedule.run_pending()
    time.sleep(1)
        