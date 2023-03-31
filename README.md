# Fansale Tracker

Fansale Tracker is a script for tracking new ticket resales in [fanSALE](https://www.fansale.de/fansale/), Eventim's official concert ticket resale platform.

## Installation

Download FireFox webdriver ([geckodriver](https://github.com/mozilla/geckodriver/releasesk)) and add it to PATH.

Use pip to install the required packages.

```sh
$ python3 -m pip install -r requirements.txt
```

## Usage

Replace the values of `.env`

```sh
FANSALE_URL=fansale_url
DISCORD_WEBHOOK_URL=your_discord_webhook_url
DISCORD_USER_ID=your_discord_user_id
```

Run

```sh
$ python3 fansale.py
```

Using cron to run automatically once every minute

```sh
$ crontab -e
```

```sh
* * * * * export DISPLAY=:0 && /path/to/python3 /path/to/fansale.py
```
