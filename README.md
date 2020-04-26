# Paragraph Bot

Paragraph Bot is a configurable Reddit bot that can detect walls of text and attempt to break them into paragraphs for easier readability.

## Configuration

Paragraph Bot uses a config file containing JSON located in `config.json`.

### `config.json`:

Here, you'll define your bot's user account, password, and Reddit script details. You can also configure how the bot captures walls of text:

```json
{
  "bot_username": "bot_username",
  "bot_password": "bot_password",
  "bot_client_id": "bot_client_id",
  "bot_client_secret": "bot_client_secret",
  "bot_user_agent": "bot_user_agent",
  "subreddit": "gravelcyclingsandbox",
  "sentence_threshold": 15,
  "minimum_sentence_length": 5,
  "response_header": "^Hi! ^I'm ^a ^bot ^and ^it ^looks ^like ^you've ^posted ^a ^wall ^of ^text. ^Here's ^my ^attempt ^to ^make ^it ^more ^readable:"
}
```

`sentence_threshold` is the number of sentences without newlines that the bot recognizes as a wall of text. Set this to a high number, then you can bring it down to something more sensitive.

`minimum_sentence_length` is the minimum characters that a sentence can contain. It's mainly used to catch acronyms and short sentences that don't necessarily need to be broken out into a new paragraph.

`response_header` is how your bot will reply to each submission. You can customize it with a short description of what the bot is doing. You can also leave it blank if you don't need this.

# Usage

After configuration, simply run `python bot.py` and watch your bot work!

You can edit any of the parameters in any of the configuration files and the bot will hot reload and use the new config on the next available post time.
