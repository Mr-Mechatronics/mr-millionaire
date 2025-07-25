# Mr. Millionaire

**Mr. Millionaire** is a console-based quiz game inspired by *Who Wants to Be a Millionaire?*, featuring 15 challenging questions, prize progression, lifelines, and AI-generated questions via LiteLLM.


---

## Features

* ✯ 15-question challenge with increasing prize money
* 🧠 AI-generated questions using LiteLLM integration
* 📀 Caches config, history, and environment in `~/.mr-millionaire`
* 🧠 Lifelines:

  * **50-50**: Eliminate two wrong options
  * **Phone a Friend**: Ask an AI friend for help
* 📊 Game history and last played session tracking
* 🔧 Configurable via CLI or config manager

---

## Installation

```bash
pip install mr-millionaire
```

---

## Running & Configuring

```bash
mr-millionaire
```

On running the game you'll be asked for 4 options.

```
Choose one from options:
  [1] Play Game
  [2] Clear Memory
  [3] Configuration
  [4] Show History
```

* [1] You can start playing the game. (for the first time it will ask you to setup LLM API Keys and MODEL name.)
* [2] Clears the memory of previously asked questions.
* [3] You can use this configuration manager to configure your LLM or difficulty of a game.
* [4] This will show previously won sheets.

---

### Things to know
---

On first run, a cache/config folder will be created automatically on playing the game:

```bash
~/.mr-millionaire/
```

It will ask for the environemnt variable name & key.

```
# Example:
LLM Environment Variable Name : GROQ_API_KEY
LLM Environment Variable Value : <your_api_key>
LLM Model (eg: groq/gemma2-9b-it) : groq/gemma2-9b-it
```

Please go through 'https://docs.litellm.ai/docs/providers' before giving the llm environment values.

---

## Configuration Options

Manage settings such as:

* Preferred LLM model
* Cache clearing
* History viewing

All settings and history are stored in `~/.mr-millionaire` you can take a look into it for further debugging.

---

## Tech Stack

* Python 3.12
* [LiteLLM](https://github.com/BerriAI/litellm) for AI-powered question generation
* `dotenv` for environment variable management
* Local filesystem storage for config and history

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
