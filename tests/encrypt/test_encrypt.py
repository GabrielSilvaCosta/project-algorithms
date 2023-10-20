from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("flamengo", 2) == "ognema_lf"

    assert encrypt_message("flamengo", 3) == "alf_ognem"

    assert encrypt_message("flamengo", 10) == "ognemalf"

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("flamengo", "a")
