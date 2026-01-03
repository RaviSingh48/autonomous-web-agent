from playwright.async_api import async_playwright
from urllib.parse import quote_plus

class Executor:
    async def run(self, step: str):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()

            if "Search" in step:
                query = step.replace("Search DuckDuckGo for", "").strip()
                encoded_query = quote_plus(query)

                search_url = f"https://duckduckgo.com/?q={encoded_query}&t=h_&ia=web"
                await page.goto(search_url, timeout=60000)

                # Wait for results to load
                await page.wait_for_timeout(5000)

            print("\n✅ Search completed.")
            input("🔵 Press ENTER to close the browser...")

            await browser.close()
            return "done"
