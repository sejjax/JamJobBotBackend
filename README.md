<h1 align="center">JamJobBot - Help process HR easier</h1>
<p align="center" style="font-style: italic; font-size: 17px">JamJobBot help you process these similar HR and <br/>ask on their similiar questions</p>
<p align="center" style="font-size: 18px; font-weight: 700;"><a href="https://sejjax.notion.site/JamJobBot-38a7369bbc314c039c7b9f44cbdf1245">📕Documentation</a> and <a href="https://t.me/JamJobBot">🤖JamJobBot</a></p>
<hr/>

## Project Structure
- `app/controllers` Contain http handlers
- `app/filters` Contain filters for bot
- `app/handlers` Contain handlers for messages
- `app/keyboard` Contain different types of keyboard
- `misc` Contain utils and helper functions
- `models` Contain DB models
- `services` Contain business logic 
- `systemd` Contain Systemd script to running bot
- `temp` Contain session files
- `test` Contain tests for whole app

### What there do?
- Read all messages from HR in Telegram, extract interview time, date, link and create notification for that time.
- Answer on the questions by HR
- Notify about new interview

