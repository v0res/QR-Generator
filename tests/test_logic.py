from core.logic import clean_filename

def test_clean_filename_standard():
    assert clean_filename("https://google.com/search") == "google_com_search"

def test_clean_filename_cyrillic():
    assert clean_filename("https://яндекс.рф") == "яндекс_рф"

def test_clean_filename_empty():
    assert clean_filename("") == ""