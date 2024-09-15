import asyncio
import os
import threading
import time
from playwright.async_api import async_playwright
from telethon import TelegramClient, events

import IDs

# Your Telegram credentials
api_id = IDs.api_id
api_hash = IDs.api_hash
bot_token = IDs.bot_token

# Telegram channel/group ID
channel_id = IDs.channel_id
group_id = IDs.group_id
event_queue = asyncio.Queue()

event_number = 0

client = TelegramClient('session', api_id, api_hash).start(bot_token=bot_token)


def open_browser():
    print("Opening Browser")
    command = "chrome.exe --remote-debugging-port=9988 --user-data-dir=..\\chromedata"
    try:
        cwd = "Application"
        os.chdir(cwd) if cwd else None
        result = os.system(command)
        if result == 0:
            print("Command executed successfully.")
        else:
            print(f"Command failed with error code {result}.")
    except OSError as e:
        print(f"Error running command: {e}")


def run():
    print("Running Thread for Browser")
    time.sleep(2)
    t: threading
    t = threading.Thread(target=open_browser)
    t.start()
    t.join(timeout=2)
    os.chdir('..')
    return "Browser Launched"


async def whatsapp(message, event_num):
    print("Whatsapp Playwright process")
    time.sleep(event_num * 20)
    async with async_playwright() as pw:
        browser = await pw.chromium.connect_over_cdp("http://localhost:9988")
        context = browser.contexts[0]
        page = context.pages[0]
        await page.goto("https://web.whatsapp.com")
        while True:
            try:
                await page.locator("//div[@role='textbox']").click()
                break
            except:
                await asyncio.sleep(5)
        await page.locator("//div[@role='textbox']").fill("Aaryaman")
        await page.locator("//div[@role='textbox']").press("Enter")
        await asyncio.sleep(2)
        await page.locator("//*[@aria-placeholder='Type a message']").fill(message)
        await page.keyboard.press("Enter")
        await page.keyboard.press("Escape")


@client.on(events.NewMessage)
async def handler(event):
    global event_number
    message_text = event.message.text
    event_number += 1
    print(f"New message detected: Event {event_number}, {message_text}")
    await whatsapp(message_text, event_number)
    event_number -= 1
    print("Event completed")


run()
print("Bot is running")
client.run_until_disconnected()
