# Universal-Telegram-Bot

TODO:
    


## Welcome scenario

Handles `/start` and sends a short intro message about the bot.

**Location:** `scenarios/welcome/`

| File | Role |
|------|------|
| `texts.py` | Reply text (`START_TEXT`) |
| `handlers.py` | `/start` handler (`Router`) |
| `__init__.py` | Exports `router` |

**Flow:** User sends `/start` → bot replies with `START_TEXT`.

**Setup:** Router is registered in `main.py` via `dp.include_router(welcome_router)`.

**Customize:** Edit `START_TEXT` in `scenarios/welcome/texts.py`.