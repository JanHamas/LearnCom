from playwright.async_api import async_playwright
from playwright_stealth import Stealth
import asyncio
import json

async def main():
    async with Stealth().use_async(async_playwright()) as p:
        # Launch browser in headed mode with appropriate settings
        browser = await p.chromium.launch(headless=False)
        
        # Create a context with mobile emulation
        
        iphone_12 = p.devices['iPhone 12']
        context = await browser.new_context(**iphone_12, permissions=["microphone"])
        
        # Apply stealth techniques
        page = await context.new_page()        
        web_page = "https://elevenlabs.io/conversational-ai?utm_source=google&utm_medium=cpc&utm_campaign=t1t2t3_youtube_conversationalai_english&utm_id=22183073408&utm_term=&utm_content=conversationalal&gad_source=2&gclid=CjwKCAjwwLO_BhB2EiwAx2e-3z4KtFiiUKx3EyObxW0zRve3PrD9O_ZnJr8rag9qsMVimsq_pTH_5xoCmpoQAvD_BwE"
        
        while True:
            try:
                print("Navigating to ElevenLabs...")
                await page.goto(web_page, wait_until="load", timeout=60000)
                
                # Wait for and click the button with more specific selector
                print("Waiting for talk button...")
                await asyncio.sleep(3)
                await page.locator("div.flex.gap-6 button").last.click()
                print("Successfully clicked on 'Talk to an agent' button")

                
                # Wait for 9 minutes with periodic checks
                for i in range(59): 
                    await asyncio.sleep(8)
                    # Check if we're still on the call page
                    if "conversational-ai" not in page.url:
                        print("No longer on call page, breaking out of loop")
                        break
                
                print("Reloading page for new session...")
                await page.reload()
                
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                print("Reloading and retrying...")
                await page.reload()
                await asyncio.sleep(5)

asyncio.run(main())