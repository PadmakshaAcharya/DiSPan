from project import generate_sequence, sequence_to_string, check_answer


def test_generate_sequence():
    result = generate_sequence(5)
    assert len(result) == 5
    assert all(digit.isdigit() for digit in result)

    result = generate_sequence(1)
    assert len(result) == 1


def test_sequence_to_string():
    assert sequence_to_string(["5", "2", "8"]) == "528"
    assert sequence_to_string(["0"]) == "0"
    assert sequence_to_string([]) == ""


def test_check_answer():
    assert check_answer("528", "528") is True
    assert check_answer("528", "529") is False
    assert check_answer("", "") is True
