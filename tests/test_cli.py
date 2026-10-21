from factorial_app.__main__ import main


def test_cli_prints_result(capsys):
    assert main(["5"]) == 0
    assert capsys.readouterr().out.strip() == "120"


def test_cli_zero(capsys):
    assert main(["0"]) == 0
    assert capsys.readouterr().out.strip() == "1"


def test_cli_negative_number(capsys):
    assert main(["-3"]) == 1
    assert "Помилка" in capsys.readouterr().err


def test_cli_not_a_number(capsys):
    assert main(["abc"]) == 1
    assert "не є цілим числом" in capsys.readouterr().err


def test_cli_wrong_argument_count(capsys):
    assert main([]) == 2
    assert main(["1", "2"]) == 2
    assert "Використання" in capsys.readouterr().err
