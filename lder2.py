import asyncio
import os
import random
import sys
import time
import shutil
from playwright.async_api import async_playwright

# ================= HIGH-SPEED CONFIGURATION =================
DEFAULT_SID = ["78070493721%3ArjTP0LdO0ZmAh6%3A10%3AAYja0bE0ws2xW1M7_15HOo6-k8ZQse2Bi7Fs45uzXg"]
DEFAULT_URL = "https://www.instagram.com/direct/t/873343335055426/"
DEFAULT_OPPONENT = "CMWF//DRAKE//BULLET//ABUSIVE//"
target = "CMWF//DRAKE//BULLET//ABUSIVE// "  # RESTORED: Target variable for default settings
DEFAULT_ENGINE_COUNT = 6
DELAY = 0.05 
# ============================================================

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def professional_banner():
    clear()
    banner = f"""
    \033[95m    ██╗     ███████╗ █████╗ ██████╗ ███████╗██████╗ 
    \033[94m    ██║     ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
    \033[96m    ██║     █████╗  ███████║██║  ██║█████╗  ██████╔╝
    \033[94m    ██║     ██╔══╝  ██╔══██║██║  ██║██╔══╝  ██╔══██╗
    \033[95m    ███████╗███████╗██║  ██║██████╔╝███████╗██║  ██║
    \033[0m
    \033[1;37m        💀 LEADER GOD IG SPAM V1 | TURBO MODE 💀
    \033[1;31m        --------------------------------------------
    \033[1;33m        DEVELOPER : LEADER GOD
    \033[1;31m        --------------------------------------------
    \033[0m"""
    print(banner)

STRIKE_MESSAGES = [
    "🖤 [{target}] 𝐆ᴜʟᴀᴀᴍɪ 𝐊ᴀʀ LEADER GOD-  † 💋 अब्बु !♡ 𝐊ɪ🎀",
    "💚 [{target}] ⋆ ִֶָ ๋𓂃 ⋆Bʜᴇɴ Kᴇ ʙʜᴏsᴅᴇ⋆ ִֶָ ๋𓂃 ⋆🎀",
    "🤍 [{target}] ⋆ ִֶָ ๋𓂃 ⋆Pʀᴇᴛᴛʏ Lɪᴛᴛʟᴇ Rᴀɴᴅɪ⋆ ִֶָ ๋𓂃🎀 ⋆",
    "🩷 [{target}] ᴛᴍᴋᴄ ᴍᴇʜ 🇱 🇦 🇳 🇩 🅳︎🅰︎🅻︎🅺︎🅴︎ 𝙛𝙖𝙖𝙙 ᴅᴜɴɢᴀ🎀",
    "🩶 [{target}] ⋆ ִֶָ ๋𓂃 ⋆𝐊ᴍ𝐳ᴏʀ ᴩɪɪʟʟᴇ⋆ ִֶָ ๋𓂃 ⋆🎀",
    "❤‍🔥 [{target}] 𝐒ᴀʏ LEADER GOD-  † 💋 अब्बु !♡",
    "🩵 [{target}] ⋆ ִֶָ ๋𓂃 ⋆𝐔ᴛʜ 𝐏ɪʟʟᴇ ⋆ ִֶָ ๋𓂃 ⋆🎀",
    "💝 [{target}] ⋆ ִֶָ ๋𓂃 ⋆𝐓ᴇʀɪ 𝐌ᴀᴀ LEADER GOD 𝐂ʜᴏᴅᴇ ⋆ ִֶָ ๋𓂃 ⋆🎀",
    "🧡 [{target}] 𝐊ɪ 𝐂𝖍𝖚𝖉𝖆𝖎 𝘉ʏ LEADER GOD-  † 💋 अब्बु !♡ ~‹‹‹★🎀",
    "💘 [{target}] ⋆ ִֶָ ๋𓂃 ⋆𝐒ᴀʏ LEADER GOD𖤍 ʙᴀᴀᴘ๋𓂃 ⋆🎀",
    "❤ [{target}] ⋆ ִֶָ ๋𓂃 ⋆𝐋ᴏᴡ 𝐋ᴇ𝐯ᴇʟ 𝐊ᴜᴛᴛʏ𓂃 ⋆🎀",
    "💖 [{target}] ⋆ ִֶָ ๋𓂃 ⋆𝐁ɪʜᴀʀɪ 𝐋ᴜɴᴅ 𝐂ʜᴏᴏs𓂃 ⋆🎀"
]

def countdown(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write(f"\r\033[1;32m    [SYSTEM] LEADER GOD DEPLOYING ENGINES IN {i} SECONDS... \033[0m")
        sys.stdout.flush()
        time.sleep(1)
    print("\n")

def get_payload(opponent):
    rand_id = random.randint(0, 9999)
    gap1_lines = "\n" * 80
    gap2_lines = "\n" * 80
    core = random.choice(STRIKE_MESSAGES).replace("{target}", opponent)
    return f"{core}{gap2_lines}{core}{gap1_lines}{core}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~LEADER GOD- † 💋 अब्बु !♡ SE CUDO ~ [{opponent}] [{rand_id}]🌀"

async def block_media(route):
    if route.request.resource_type in ["image", "media", "font"]:
        await route.abort()
    else:
        await route.continue_()

async def force_name_lock(page, gc_name):
    try:
        gear = page.locator('svg[aria-label="Conversation information"]')
        await gear.click()
        change_btn = page.locator('div[aria-label="Change group name"][role="button"]')
        group_input = page.locator('input[aria-label="Group name"][name="change-group-name"]')
        save_btn = page.locator('div[role="button"]:has-text("Save")')
        await change_btn.click()
        await group_input.fill(gc_name)
        if await save_btn.is_enabled():
            await save_btn.click()
            print(f"\033[1;32m    🔒 [LOCK] NAME RESET TO: {gc_name}\033[0m")
        await gear.click()
    except Exception:
        await page.reload()

async def run_engine(engine_id, sid, url, opponent, gc_name, is_locker):
    user_data_dir = f"./session_data_{engine_id}"
    while True:
        async with async_playwright() as p:
            browser = await p.chromium.launch_persistent_context(
                user_data_dir, headless=True,
                args=["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"]
            )
            await browser.add_cookies([{"name": "sessionid", "value": sid, "domain": ".instagram.com", "path": "/", "secure": True, "httpOnly": True}])
            page = await browser.new_page()
            await page.route("**/*", block_media)
            try:
                await page.goto(url, wait_until='domcontentloaded', timeout=60000)
                msg_box = page.locator('div[role="textbox"], div[aria-label="Message"]').first
                
                msg_count = 0
                while True: 
                    if msg_count > 0 and msg_count % 50 == 0:
                        await page.reload(wait_until='domcontentloaded')
                        msg_box = page.locator('div[role="textbox"], div[aria-label="Message"]').first
                        await msg_box.focus()

                    if is_locker and msg_count >= 19:
                        await force_name_lock(page, gc_name)
                        msg_count = 0
                        await msg_box.focus()
                    
                    await msg_box.focus()
                    await msg_box.fill(get_payload(opponent)) 
                    await page.keyboard.press("Enter")
                    
                    msg_count += 1
                    status = "\033[1;35mLOCKER\033[0m" if is_locker else "\033[1;36mSLAMMER\033[0m"
                    print(f"    \033[1;37m[E-{engine_id}] [{status}] STRIKE: {msg_count} | BY LEADER GOD\033[0m")
                    
                    await asyncio.sleep(random.uniform(DELAY, DELAY + 0.02))
                    
            except Exception:
                print(f"    ⚠️ [E-{engine_id}] RELOADING ENGINE...")
            
            await browser.close()
            if os.path.exists(user_data_dir):
                shutil.rmtree(user_data_dir, ignore_errors=True)
            await asyncio.sleep(1)

async def main():
    professional_banner()
    choice = input("\033[1;37m    🌀 USE DEFAULT SETTINGS BY LEADER GOD? (y/n): \033[0m").strip().lower()
    
    if choice in ['y', 'yes']:
        sids, url, opponent, engine_count = DEFAULT_SID, DEFAULT_URL, DEFAULT_OPPONENT, DEFAULT_ENGINE_COUNT
    else:
        multi = input("    🌀 MULTI-ID MODE? (y/n): ").strip().lower()
        if multi in ['y', 'yes']:
            sids = [s.strip() for s in input("    🌀 SESSIONS (comma separated): ").split(',')]
        else:
            sids = [input("    🌀 SESSION ID: ").strip()]
        url = input("    🌀 GROUP URL: ").strip()
        opponent = input("    🌀 OPPONENT NAME: ").strip()
        engine_count = int(input("    🌀 ENGINE COUNT (3-6): ").strip() or 4)

    gc_name = f"[{opponent}] ᵗᵉʳⁱ ᵐᵃᵃᴄʜɪɴꫝʟ (😂)"
    professional_banner()
    countdown(3)
    
    tasks = [run_engine(i+1, sids[i % len(sids)], url, opponent, gc_name, i == 0) for i in range(engine_count)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\033[1;31m   LEADER GOD-  † 💋 अब्बु !♡ 𝐕𝟷 𝐔ʟᴛʀᴀ 𝐓ᴇʀᴍɪɴᴀᴛᴇᴅ 𝐒ᴜᴄᴄᴇssғᴜʟʟʏ 🌀 \033[0m")
        sys.exit()