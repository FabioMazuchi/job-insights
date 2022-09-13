from src.counter import count_ocurrences


def test_total_palavras_python():
    assert count_ocurrences("src/jobs.csv", "Python") == 1639


def test_total_palavras_python_minusculas():
    assert count_ocurrences("src/jobs.csv", "python") == 1639


def test_total_palavras_javascript():
    assert count_ocurrences("src/jobs.csv", "Javascript") == 122


def test_total_palavras_javascript_minusculas():
    assert count_ocurrences("src/jobs.csv", "javascript") == 122
