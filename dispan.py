import pyttsx3
import random
import sys

global SEQUENCE_LENGTH
SEQUENCE_LENGTH = 1

global MISTAKE_COUNT
MISTAKE_COUNT = 0

def generate_sequence(length):
    sequence = []
    for _ in range(length):
        sequence.append(str(random.randint(0, 9)))
    return sequence

def sequence_to_string(sequence):
    result = ""
    for digit in sequence:
        result += digit
    return result

def check_answer(user_input, correct_sequence):
    return user_input == correct_sequence

def speak_sequence(sequence):
    engine = pyttsx3.init()
    engine.setProperty('rate', 115)
    engine.say(sequence)
    engine.runAndWait()


def main():
    try:
        global SEQUENCE_LENGTH
        global MISTAKE_COUNT

        sequence = generate_sequence(SEQUENCE_LENGTH)
        sequence_str = sequence_to_string(sequence)
        speak_sequence(sequence)

        user_input = input("Enter sequence: ")

        if check_answer(user_input, sequence_str):
            SEQUENCE_LENGTH += 1
            MISTAKE_COUNT = 0
            return main()
        else:
            MISTAKE_COUNT += 1
            if MISTAKE_COUNT < 2:
                return main()
            else:
                print(f"Max digits: {SEQUENCE_LENGTH - 1}")

    except KeyboardInterrupt:
        sys.exit(f"\nInterrupted. Max digits: {SEQUENCE_LENGTH - 1}")
    except Exception:
        sys.exit(f"Max digits: {SEQUENCE_LENGTH - 1}")


if __name__ == "__main__":
    main()
