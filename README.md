# My Telegram Bot

A simple Telegram bot using **Telethon** that can:

* Solve math equations with `/slove`
* Compare two numbers with `/compare`
* Use the Collatz Conjecture with `/collatz`

---

## Setup

1. **Clone the repository**:

   ```
   git clone https://github.com/AmirNakheSabz/telegram-math-bot.git
   cd telegram-math-bot
   ```

2. **Create a virtual environment** (recommended):

   ```
   python -m venv venv
   ```

   * On macOS/Linux:

     ```
     source venv/bin/activate
     ```
   * On Windows (PowerShell):

     ```
     venv\Scripts\Activate.ps1
     ```

3. **Install dependencies**:

   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:

   * Copy `.env.example` to `.env`:

     ```
     cp .env.example .env
     ```
   * Open `.env` and add your own `API_ID`, `API_HASH`, and `BOT_TOKEN`.

5. **Run the bot**:

   ```
   python bot.py
   ```

---

## Usage

* `/slove <equation>`
  Solve a simple equation.
  Example:

  ```
  /slove 2*x+1=5
  ```

* `/compare <num1> <num2>`
  Compare two numbers.
  Example:

  ```
  /compare 5 10
  ```

* `/collatz <n>`
    Use Collatz Conjecture
    Example:

    ```
    /collatz 27
    ```

---

## Requirements

* Python 3.8+
* Dependencies listed in `requirements.txt`

  * telethon
  * sympy
  * python-dotenv

---
