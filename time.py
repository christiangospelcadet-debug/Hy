"""
Install:  pip install playwright playwright-stealth
          playwright install chromium
Run:      python arnav_masterpiece.py
"""

import asyncio
import gc
import json
import random
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from playwright.async_api import async_playwright
from playwright_stealth import stealth

# IST = UTC+5:30
IST = timezone(timedelta(hours=5, minutes=30))

def ist_now() -> str:
    """Returns current IST time as HH:MM:SS:ms"""
    n = datetime.now(IST)
    return f"{n.hour:02d}:{n.minute:02d}:{n.second:02d}:{n.microsecond // 1000:03d}"

MESSAGES = [
    "\n".join(["[{t}] [{time}] 𝒀𝒆 𝑹𝒂𝒏𝒅𝒊 𝒌𝒊 𝑴𝒂 𝒀𝒂𝒉 𝑻𝒊𝒎𝒆 𝑴𝒆𝒊𝒏 𝑪𝒉𝒖𝒅𝒊 𝑻𝒉𝒊   𓆩🦋𓆪\n\n\n"] * 9),
    "\n".join(["[{t}] [{time}] 𝒀𝒆 𝑹𝒂𝒏𝒅𝒊 𝒌𝒊 𝑴𝒂 𝒀𝒂𝒉 𝑻𝒊𝒎𝒆 𝑴𝒆𝒊𝒏 𝑪𝒉𝒖𝒅𝒊 𝑻𝒉𝒊   𓆩🦩𓆪\n\n\n"] * 9),
    "\n".join(["[{t}] [{time}] 𝒀𝒆 𝑹𝒂𝒏𝒅𝒊 𝒌𝒊 𝑴𝒂 𝒀𝒂𝒉 𝑻𝒊𝒎𝒆 𝑴𝒆𝒊𝒏 𝑪𝒉𝒖𝒅𝒊 𝑻𝒉𝒊   𓆩🐞𓆪\n\n\n"] * 9),
    "\n".join(["[{t}] [{time}] 𝒀𝒆 𝑹𝒂𝒏𝒅𝒊 𝒌𝒊 𝑴𝒂 𝒀𝒂𝒉 𝑻𝒊𝒎𝒆 𝑴𝒆𝒊𝒏 𝑪𝒉𝒖𝒅𝒊 𝑻𝒉𝒊   𓆩🐛𓆪\n\n\n"] * 9),
    "\n".join(["[{t}] [{time}] 𝒀𝒆 𝑹𝒂𝒏𝒅𝒊 𝒌𝒊 𝑴𝒂 𝒀𝒂𝒉 𝑻𝒊𝒎𝒆 𝑴𝒆𝒊𝒏 𝑪𝒉𝒖𝒅𝒊 𝑻𝒉𝒊   𓆩🐝𓆪\n\n\n"] * 9),
    "\n".join(["[{t}] [{time}] 𝒀𝒆 𝑹𝒂𝒏𝒅𝒊 𝒌𝒊 𝑴𝒂 𝒀𝒂𝒉 𝑻𝒊𝒎𝒆 𝑴𝒆𝒊𝒏 𝑪𝒉𝒖𝒅𝒊 𝑻𝒉𝒊   𓆩🐦𓆪\n\n\n"] * 9),
    "\n".join(["[{t}] [{time}] 𝒀𝒆 𝑹𝒂𝒏𝒅𝒊 𝒌𝒊 𝑴𝒂 𝒀𝒂𝒉 𝑻𝒊𝒎𝒆 𝑴𝒆𝒊𝒏 𝑪𝒉𝒖𝒅𝒊 𝑻𝒉𝒊   𓆩🦄𓆪\n\n\n"] * 9),
    "\n".join(["[{t}] [{time}] 𝒀𝒆 𝑹𝒂𝒏𝒅𝒊 𝒌𝒊 𝑴𝒂 𝒀𝒂𝒉 𝑻𝒊𝒎𝒆 𝑴𝒆𝒊𝒏 𝑪𝒉𝒖𝒅𝒊 𝑻𝒉𝒊   𓆩🦥𓆪\n\n\n"] * 9),
    "\n".join(["[{t}] [{time}] 𝒀𝒆 𝑹𝒂𝒏𝒅𝒊 𝒌𝒊 𝑴𝒂 𝒀𝒂𝒉 𝑻𝒊𝒎𝒆 𝑴𝒆𝒊𝒏 𝑪𝒉𝒖𝒅𝒊 𝑻𝒉𝒊   𓆩🐦‍🔥𓆪\n\n\n"] * 9),
    "\n".join(["[{t}] [{time}] 𝒀𝒆 𝑹𝒂𝒏𝒅𝒊 𝒌𝒊 𝑴𝒂 𝒀𝒂𝒉 𝑻𝒊𝒎𝒆 𝑴𝒆𝒊𝒏 𝑪𝒉𝒖𝒅𝒊 𝑻𝒉𝒊   𓆩🦢𓆪\n\n\n"] * 9),
]

PROFILES_DIR   = Path.home() / "arnav_ig_profiles"
ACCOUNTS_FILE  = Path.home() / "arnav_ig_accounts.json"
PRIMARY_SELECTOR = 'div[role="textbox"]'

MOBILE_UA       = "Mozilla/5.0 (Linux; Android 13; vivo V60) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36"
MOBILE_VIEWPORT = {"width": 412, "height": 915}

FAST_ARGS = [
    "--disable-dev-shm-usage", "--no-sandbox", "--disable-gpu",
    "--disable-setuid-sandbox", "--disable-extensions", "--disable-sync",
    "--disable-background-networking", "--disable-background-timer-throttling",
    "--disable-renderer-backgrounding", "--disable-web-security",
    "--disable-features=IsolateOrigins,site-per-process", "--mute-audio",
    "--disable-logging", "--disable-breakpad", "--disable-blink-features=AutomationControlled",
]

_SEL = json.dumps(PRIMARY_SELECTOR)

# FIXED: Escaped curly braces for JS Fill
JS_FILL = f"""
(text) => {{
    const el = document.querySelector({_SEL});
    if (!el) return null;
    const wasEmpty = el.innerText.trim() === '';
    el.focus();
    document.execCommand('selectAll', false, null);
    const dt = new DataTransfer();
    dt.setData('text/plain', text);
    el.dispatchEvent(new ClipboardEvent('paste', {{
        clipboardData: dt,
        bubbles: true,
        cancelable: true
    }}));
    return wasEmpty;
}}
"""

BURST_SIZE = 20

class AccountManager:
    def __init__(self):
        PROFILES_DIR.mkdir(parents=True, exist_ok=True)
        self.accounts = self._load()

    def _load(self):
        if ACCOUNTS_FILE.exists():
            try:
                with open(ACCOUNTS_FILE, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

    def _save(self):
        with open(ACCOUNTS_FILE, 'w') as f:
            json.dump(self.accounts, f, indent=2)

    def add(self, username):
        if username in [a['username'] for a in self.accounts]:
            print(f"  ⚠️  @{username} already exists")
            return
        self.accounts.append({
            'username': username,
            'profile_dir': str(PROFILES_DIR / f"acc_{len(self.accounts)+1}_{username}"),
            'logged_in': False
        })
        self._save()
        print(f"  ✅ @{username} added")

    def mark_logged_in(self, username):
        for a in self.accounts:
            if a['username'] == username:
                a['logged_in'] = True
        self._save()

    def list(self):
        if not self.accounts:
            print("\n  📋 No accounts yet. Add one first.")
            return
        print("\n  📋 ACCOUNTS:")
        for i, a in enumerate(self.accounts, 1):
            status = "✅ Ready" if a.get('logged_in') else "⚠️  Need Login"
            print(f"     {i}. @{a['username']}  [{status}]")

    def logged_in(self):
        return [a for a in self.accounts if a.get('logged_in')]

    async def do_login(self, idx):
        if idx < 0 or idx >= len(self.accounts):
            print("  ❌ Invalid account number"); return
        acc = self.accounts[idx]
        print(f"\n  🔐 Opening browser for @{acc['username']}...")
        print(f"  👉 Log in manually then press ENTER here\n")
        input("  Press ENTER to open browser → ")
        async with async_playwright() as p:
            browser = await p.chromium.launch_persistent_context(
                user_data_dir=acc['profile_dir'],
                headless=False,
                args=['--no-sandbox', '--disable-blink-features=AutomationControlled'],
                user_agent=MOBILE_UA,
                viewport=MOBILE_VIEWPORT,
                is_mobile=True,
                has_touch=True,
                ignore_https_errors=True
            )
            page = browser.pages[0] if browser.pages else await browser.new_page()
            await page.goto('https://www.instagram.com/', timeout=60000)
            print(f"\n  Browser opened! Log in to @{acc['username']}")
            input("\n  Done logging in? Press ENTER → ")
            await asyncio.sleep(2)
            logged = "/accounts/login" not in page.url
            if not logged:
                confirm = input("  Couldn't verify. Are you logged in? (y/n): ").lower()
                logged = confirm == 'y'
            if logged:
                self.mark_logged_in(acc['username'])
                print(f"  ✅ @{acc['username']} session saved!")
            else:
                print(f"  ❌ Login not confirmed")
            await browser.close()

DOM_FLUSH_INTERVAL  = 300
WORKER_RETRY_DELAY  = 3
TAB_RETRY_DELAY     = 5
ACCOUNT_RETRY_DELAY = 15
BLOCK_BACKOFF_BASE  = 30
BLOCK_BACKOFF_MAX   = 1800
LOGOUT_RETRY_MAX    = 5

class MasterSpammer:
    def __init__(self, url, target, accounts, pages_per_account):
        self.url               = url
        self.target            = target
        self.accounts          = accounts
        self.pages_per_account = pages_per_account
        self.running           = True
        self.total_sent        = 0
        self.total_failed      = 0
        self.start_time        = None
        self.account_stats     = {}
        self.line_templates = [
            [line.replace("{t}", target) for line in m.split("\n")]
            for m in MESSAGES
        ]
        self.pool_size = len(self.line_templates)

    def _next_msg(self) -> str:
        t = ist_now()
        tmpl = self.line_templates[random.randrange(self.pool_size)]
        return "\n".join(line.replace("{time}", t) for line in tmpl)

    # FIXED: Escaped curly braces for the JS MutationObserver
    async def _wait_stable_input(self, page, timeout=12):
        try:
            await page.evaluate(f"""
                () => new Promise((resolve, reject) => {{
                    const sel = {_SEL};
                    const find = () => {{
                        const el = document.querySelector(sel);
                        if (!el) return null;
                        const r = el.getBoundingClientRect();
                        return (r.width > 0 && r.height > 0) ? el : null;
                    }};
                    if (find()) {{ resolve(true); return; }}
                    const obs = new MutationObserver(() => {{
                        if (find()) {{ obs.disconnect(); resolve(true); }}
                    }});
                    obs.observe(document.body, {{ childList: true, subtree: true }});
                    setTimeout(() => {{ obs.disconnect(); reject('timeout'); }}, {timeout * 1000});
                }})
            """)
            return True
        except:
            return False

    async def _js_fill(self, page, text: str):
        return await page.evaluate(JS_FILL, text)

    async def _is_logged_out(self, page):
        try:
            url = page.url
            if "/accounts/login" in url or "/login" in url: return True
            login_el = await page.query_selector('input[name="username"]')
            return login_el is not None
        except: return False

    async def _is_rate_limited(self, page):
        try:
            if self.url.split("?")[0] in page.url:
                el = await page.query_selector(PRIMARY_SELECTOR)
                return el is None
        except: pass
        return False

    async def _send_worker(self, page, username):
        acc_stat = self.account_stats[username]
        fails, backoff, input_ok = 0, BLOCK_BACKOFF_BASE, False
        while self.running:
            try:
                if not input_ok:
                    if not await self._wait_stable_input(page, timeout=15):
                        if await self._is_logged_out(page):
                            print(f"\n  🔐 [@{username}] Logged out — backoff {backoff}s")
                            await asyncio.sleep(backoff)
                            backoff = min(backoff * 2, BLOCK_BACKOFF_MAX)
                            try: await page.goto(self.url, timeout=30000, wait_until='domcontentloaded')
                            except: pass
                        elif await self._is_rate_limited(page):
                            print(f"\n  🚫 [@{username}] Rate limited — backoff {backoff}s")
                            await asyncio.sleep(backoff)
                            backoff = min(backoff * 2, BLOCK_BACKOFF_MAX)
                            try: await page.reload(timeout=20000, wait_until='domcontentloaded')
                            except: pass
                        else:
                            await asyncio.sleep(WORKER_RETRY_DELAY)
                        continue
                    input_ok, backoff, fails = True, BLOCK_BACKOFF_BASE, 0

                sent = 0
                for _ in range(BURST_SIZE):
                    if not self.running: break
                    result = await self._js_fill(page, self._next_msg())
                    if result is None:
                        input_ok = False; fails += 1; break
                    await page.keyboard.press("Enter")
                    sent += 1; fails = 0

                if sent:
                    self.total_sent += sent
                    acc_stat['sent'] += sent
                if fails >= 3: input_ok, fails = False, 0
                await asyncio.sleep(0)
            except Exception:
                fails += 1; input_ok = False; self.total_failed += 1
                if fails >= 5: fails = 0
                await asyncio.sleep(0)

    async def _dom_flush_manager(self, page, username):
        while self.running:
            await asyncio.sleep(DOM_FLUSH_INTERVAL)
            if not self.running: break
            try:
                await page.reload(timeout=30000, wait_until='domcontentloaded')
                gc.collect()
            except: pass

    async def _page_worker(self, browser, page_id, username):
        retry_delay = TAB_RETRY_DELAY
        while self.running:
            page = None
            try:
                page = await browser.new_page()
                await page.goto(self.url, timeout=60000, wait_until='domcontentloaded')
                if "/accounts/login" in page.url: raise Exception("Session expired")
                el = await page.wait_for_selector(PRIMARY_SELECTOR, timeout=30000, state='visible')
                if not el: raise Exception("Input not found")
                print(f"  ✅ [@{username}] Instance {page_id} ready")
                worker_task = asyncio.create_task(self._send_worker(page, username))
                flush_task  = asyncio.create_task(self._dom_flush_manager(page, username))
                await asyncio.gather(worker_task, flush_task)
            except Exception as e:
                if self.running:
                    print(f"\n  🔁 [@{username}] Instance {page_id} restarting in {retry_delay}s")
                    await asyncio.sleep(retry_delay)
                    retry_delay = min(retry_delay * 2, 60)
            finally:
                if page:
                    try: await page.close()
                    except: pass

    async def _account_worker(self, account):
        username, profile_dir = account['username'], account['profile_dir']
        self.account_stats[username] = {'sent': 0}
        logout_hits, retry_delay = 0, ACCOUNT_RETRY_DELAY
        while self.running:
            async with async_playwright() as p:
                browser = None
                try:
                    browser = await p.chromium.launch_persistent_context(
                        user_data_dir=profile_dir, headless=True, args=FAST_ARGS,
                        user_agent=MOBILE_UA, viewport=MOBILE_VIEWPORT, is_mobile=True,
                        has_touch=True, ignore_https_errors=True
                    )
                    # FIXED: Escaped curly braces in add_init_script
                    await browser.add_init_script("""
                        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
                        Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
                        window.chrome = { runtime: {} };
                    """)
                    check = await browser.new_page()
                    await check.goto('https://www.instagram.com/', timeout=60000, wait_until='domcontentloaded')
                    if "/accounts/login" in check.url:
                        logout_hits += 1; await check.close()
                        if logout_hits >= LOGOUT_RETRY_MAX: return
                        wait = min(BLOCK_BACKOFF_BASE * (2 ** logout_hits), BLOCK_BACKOFF_MAX)
                        await asyncio.sleep(wait); continue
                    logout_hits, retry_delay = 0, ACCOUNT_RETRY_DELAY
                    await check.close()
                    await asyncio.gather(*[asyncio.create_task(self._page_worker(browser, i + 1, username)) for i in range(self.pages_per_account)])
                except Exception:
                    if self.running: await asyncio.sleep(retry_delay); retry_delay = min(retry_delay * 2, 120)
                finally:
                    if browser:
                        try: await browser.close()
                        except: pass

    async def _print_stats(self):
        while self.running:
            if self.start_time:
                elapsed = time.time() - self.start_time
                speed = int(self.total_sent / elapsed * 60) if elapsed > 0 else 0
                per_acc = " | ".join([f"@{u[:10]}: {s.get('sent', 0):,}" for u, s in self.account_stats.items()])
                print(f"\r  ⚡ {self.total_sent:,} sent | {speed:,}/min | ❌ {self.total_failed} || {per_acc}   ", end='', flush=True)
            await asyncio.sleep(1.0)

    async def run(self):
        print(f"🚀 STARTING SPAM TARGETING: {self.target}")
        input("  Press ENTER to launch → ")
        self.start_time = time.time()
        account_tasks = [asyncio.create_task(self._account_worker(acc)) for acc in self.accounts]
        stats_task = asyncio.create_task(self._print_stats())
        try: await asyncio.gather(*account_tasks, stats_task)
        except asyncio.CancelledError: pass
        finally: self.running = False

async def main():
    print("ARNAV'S MASTERPIECE - IG SPAMMER")
    mgr = AccountManager()
    while True:
        print("\n 1. Add | 2. List | 3. Login | 4. 🚀 START | 5. Exit")
        choice = input("\n  Choose → ").strip()
        if choice == '1':
            u = input(" Username: ").strip()
            if u: mgr.add(u)
        elif choice == '2': mgr.list()
        elif choice == '3':
            mgr.list()
            if mgr.accounts:
                try: await mgr.do_login(int(input(" Account #: ")) - 1)
                except: print("Invalid selection")
        elif choice == '4':
            ready = mgr.logged_in()
            if not ready: continue
            raw_url = input(" IG Link/ID: ").strip()
            url = raw_url if raw_url.startswith("http") else f"https://www.instagram.com/direct/t/{raw_url}"
            target = input(" Target name: ").strip() or "target"
            pages = int(input(" Sessions (default 9): ").strip() or "9")
            spammer = MasterSpammer(url, target, ready, pages)
            try: await spammer.run()
            except KeyboardInterrupt: spammer.running = False
        elif choice == '5': break

if __name__ == "__main__":
    asyncio.run(main())