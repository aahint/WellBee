# WellBee

A **mental wellbeing web app** built with Python and Streamlit. Log in, track your mood, keep a private journal, chat with an AI companion, take personality tests and find wellbeing resources, all in one place.

## Features
| Page | What it does |
|---|---|
| **Login / Sign up** | Account creation and login. Passwords are stored as bcrypt hashes |
| **Mood Tracker** | Pick a date, choose how you feel and add a note. One entry per day, shown on a calendar |
| **My Journals** | Write journal entries by date, read them back and delete them |
| **Mental Health Companion** | Chat with an AI coach (Llama 3.1 70B). Your conversation history is saved per user |
| **Personality Tests** | MBTI, OCEAN and DISC style tests with result charts |
| **Resources** | Yoga and meditation guides with guided audio |

## Tech stack
Python · Streamlit · MySQL · Llama 3.1 (via the Krutrim API) · bcrypt · pytest · GitHub Actions

## Project structure
```
WellBee/
├── Login.py              # entry point: login and sign-up
├── pages/                # one file per Streamlit page
│   ├── Mood_Tracker.py
│   ├── My_Journals.py
│   ├── Mental_Health_Companion.py
│   ├── Personality_Tests.py
│   └── Resources.py
├── db_connection.py      # MySQL connection (reads DB_* environment variables)
├── functions.py          # login check, password hashing, chatbot call
├── commands.sql          # database schema
├── anime/                # Lottie animations
├── tests/                # pytest tests
└── .github/workflows/    # CI (tests) and deployment
```

## Database
Four tables: `users`, `mood_tracker`, `user_journals` and `user_chats`. Moods, journals and chats belong to a user by email and are deleted with the account. The schema is in `commands.sql`.

## Run it locally
```bash
git clone https://github.com/aahint/WellBee.git
cd WellBee
pip install -r requirements.txt

# 1. Create a MySQL database named MHC and run the CREATE TABLE statements in commands.sql
# 2. Create a .env file (see Configuration below)
streamlit run Login.py
```

## Configuration
Create a `.env` file in the project root:
```
API_KEY=your_krutrim_api_key
```
The database connection defaults to `localhost`, user `root`, password `root`, database `MHC`. Override any of these with the environment variables `DB_HOST`, `DB_USER`, `DB_PASSWORD` and `DB_NAME`.

## Tests
```bash
pytest tests/
```
Tests run on every push through GitHub Actions against a MySQL service.

## Roadmap
- Replace absolute file paths for images and audio with paths inside the repo
- Escape journal text before rendering it as HTML
- Mood history charts
