import re
import asyncio
from playwright.async_api import async_playwright


USERNAME = "TYPE YOUR USERNAME HERE"
PASSWORD = "TYPE YOUR PASSWORD HERE"
HOST = "zproxy.lum-superproxy.io:9222"

URL = "https://www.apolomarketing.net/" # USE YOUR URL HERE


def process(html):
    regex = re.compile("<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
    title = regex.search(html).group(1)

    print(f"Title: {title}")


async def main():
    browser_url = f"https://{USERNAME}:{PASSWORD}@{HOST}"
    async with async_playwright() as pw:
        print("Connecting to browser...")
        browser = await pw.chromium.connect_over_cdp(browser_url)

        page = await browser.new_page()

        print(f"Navigating to URL {URL}...")
        await page.goto(URL, timeout=120000)

        process(await page.evaluate("()=>document.documentElement.outerHTML"))

        await browser.close()


asyncio.run(main())