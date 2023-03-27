from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # pass
    # result1 = encrypt_message("teste", "1")
    with pytest.raises(TypeError):
        encrypt_message("teste", "1")

    # result2 = encrypt_message(2, 1)
    with pytest.raises(TypeError):
        encrypt_message(2, 1)

    assert encrypt_message("arara", 100) == "arara"

    assert encrypt_message("matheus", 3) == "tam_sueh"

    assert encrypt_message("matheus", 4) == "sue_htam"
