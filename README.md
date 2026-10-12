Hi :D

ADA is an Elo-based learning game where you build skill, and rating, by answering questions. Elo is the rating system used in chess: you gain points when you do well and lose them when you don't, so your number reflects your level.

There are a lot of ways to learn something new, from books and video lectures to one-on-one tutoring. One especially popular style is the interactive kind, like Quizlet. ADA takes that idea and adds a competitive layer to encourage learning more. New players start by proving their knowledge in test mode, and once they've earned enough Elo, they unlock ranked mode. It's mainly designed for middle and high school students.

ADA started as a hackathon idea with two teammates, @alexsalonics and @dand815. I wrote all of the code and implementation, so I'm publishing it here as its own project, with their permission.

## Status

**Working:**
- Trigonometry lessons mode. Answer questions to earn Elo.

**Next:**
- Ranked mode, unlocked once you've earned enough Elo from test mode, where you compete against other players.
- Server and accounts.
- More subjects beyond math.

## How to run

```bash
pip install django
python manage.py migrate
python manage.py runserver
```

## Built with

- Python
- CSS
- Django
   SQLite
