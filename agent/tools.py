async def extract_text(page):
    return await page.inner_text("body")
