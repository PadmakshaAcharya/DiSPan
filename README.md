# DiSpan
#### Video Demo: https://youtu.be/zp03Kh_4i5w?si=BEu7KiwRSIyCt8bN
#### Description:

DiSpan is a terminal digit span based memory test inspired by the digit span task used
in cognitive  testing. The program speaks aloud a random sequence of digits using external library for turning text to speech, 
then asks the user to type back what they heard. If correct, the sequence grows by one digit and the testcontinues. 
If incorrect, the user is given a short recovery window before the
test ends and returns the highest sequence user reached.

The goal was to build something that reflects a well known cognitive
assessment format, while implementing some core concepts from CS50P course, using third party library.

## How It Works

On each round, the program:
1. Generates a random sequence of digits at the current difficulty level.
2. Converts that sequence into a spoken and comparable string format.
3. Speaks the sequence aloud using the `pyttsx3` engine.
4. Prompts the user to type back the sequence they heard.
5. Checks whether the input matches. If correct, difficulty increases and the
   test continues. If incorrect, the user is allowed a short recovery period
   (repeating the same span of digits) before the test ends.

When the test ends, either by two consecutive mistakes or by
the user interrupting the program (Ctrl+C), the program returns the maximum
digit span the user successfully recalled.

## Files

- **`project.py`**: Contains all core logic:
  - `main()`: Orchestrates each round of the test, generating a sequence,
    speaking it, collecting user input, checking the answer, and recursively
    continuing or ending the game based on the result. It also wraps the game
    in a `try and except` block to handle unexpected errors and `KeyboardInterrupt`, 
    reporting the user's final score instead of crashing.
  - `generate_sequence(length)`: Returns a list of `length` random digits
    (strings), using Python's `random.randint()`.
  - `sequence_to_string(sequence)`: Converts a list of digit strings into a
    single string, used both for speech output and for comparing against user
    input.
  - `check_answer(user_input, correct_sequence)`: Compares the user's typed
    input against the correct sequence string and returns `True` or `False`.
  - `speak_sequence(sequence)`: Uses `pyttsx3` to read the sequence aloud at
    a speech rate of 115 words per minute.

- **`test_project.py`**: Contains pytest tests for the three functions, `generate_sequence`, `sequence_to_string` and
  `check_answer`. These were chosen for testing specifically because they
  take clear inputs and return predictable outputs.

- **`requirements.txt`**: Lists `pyttsx3`, the only third-party lbrary that
   handles offline text to speech conversion.

## Design Decisions

**Recursion instead of a loop for the game logic.** Each round of the test
calls `main()`. 
This was chosen partly to preserve state naturally through the return value chain,
and partly as a deliberate way to practice recursion, one of CS50P's core
topics, in a context where it maps intuitively onto "repeat this round with
updated parameters."

**A one-mistake recovery window.** Rather than ending the test on the very
first wrong answer (too punitive, and not reflective of how real digit span
assessments work) or allowing unlimited retries (too forgiving, and would
make the test meaningless), the program allows one mistake before requiring
two consecutive correct answers at the same difficulty level to fully
recover. This mirrors, in simplified form, the kind of tolerance built into
real short-term memory assessments, while still being simple enough to
implement with a basic mistake counter.

**Offline text-to-speech.** `pyttsx3` was chosen because it works
offline and doesn't depend on an external APIs.
