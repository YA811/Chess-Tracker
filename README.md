# Project plan

# screenshot of the app

<img src="/plan/screenshot.png">

# Idea description

chessTracker lets players keep track of their games, puzzles, and training sessions. It monitors progress by keeping track of performance, win rates, and puzzle success. The app is intended to keep gamers motivated and help them improve their chess skills over time.

# ERD


<img src="/plan/ERD.jpeg">


# User stories


- As a user I expect to to have a signup form that includes a username and password.
- As a user I want to sign in once my account is created.
- As a user I would like to create game details that has opponent name, date, result, notes. 
- As a user I want to create, delete, edit, and read any game added.
- As a user I would like to create training details that has focus, duration, date, notes. 
- As a user I expect to create, delete, edit, and read any training added.


# mock-ups


- Sign up page:

<img src="/plan/signup.jpeg">

- Sign in page:

<img src="/plan/login.jpeg">

- Home page:

<img src="/plan/homepage.jpeg">

- Game page:

<img src="/plan/game.jpeg">

- Add Game:

<img src="/plan/add game.jpeg">

- Training page:

<img src="/plan/training.jpeg">

- Add Training:

<img src="/plan/add training.jpeg">

# Pseudo code

- Define Data Structures:
    - Game:
        - result (win/loss/draw)
        - opponent_name (optional)
        - game_notes
        - date_played
    - TrainingSession:
        - focus_area (e.g., openings, endgames, puzzles)
        - duration (in hours)
        - training_notes
        - date_trained
    - User:
        - username
        - password (optional for authentication)
        - list of games
        - list of training sessions
- Development Steps:
- Game Logging:
    - def:
        - Create a form or input fields to log a game result (win/loss/draw).
        - Allow optional input for opponent's name.
        - Provide input for game notes and the date the game was played.
        - Save the logged game as a Game object with the specified attributes (result, opponent_name, game_notes, date_played).
        - Store the new Game object in the User’s list of games.
- Training Session Logging:
    - def:
        - Create a form or input fields to log a training session.
        - Allow input for focus_area (e.g., openings, endgames, puzzles).
        - Provide input for duration (in hours) and training notes.
        - Capture the date the training session took place.
        - Save the training session as a TrainingSession object with the specified attributes (focus_area, duration, training_notes, date_trained).
        - Store the new TrainingSession object in the User’s list of training sessions.

# Future work 
- adding a game analysis for the games so we can analyze them.
- adding a puzzle model so the user can practice there.

# Technologies used
- django, css, html

# app link
- https://chesstracker-7009f5cf254b.herokuapp.com/your-games/