# My Telegram Bot

A simple Telegram bot using **Telethon** that can:

* Solve math equations with `/slove`
* Compare two numbers with `/compare`

---

## Setup

1. **Clone the repository** (after you push it to GitHub):

   ```
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
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

---

## Security Notes

* Do **not** commit your `.env` file or Telethon session files to GitHub.
* Rotate your API credentials immediately if they are ever exposed.

---

## Requirements

* Python 3.8+
* Dependencies listed in `requirements.txt`

  * telethon
  * sympy
  * python-dotenv

---
