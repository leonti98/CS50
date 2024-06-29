from twttr import shorten
#import pytest

def test_shorten_Twitter():
    assert shorten("Twitter") == "Twttr"

def test_shorten_name():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_shorten_cs50():
    assert shorten("CS50") == "CS50"

def test_shorten_harry():
    assert shorten("HARRY POTTER") == "HRRY PTTR"
