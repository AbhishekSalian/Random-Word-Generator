import pytest
from RandomWordGenerator import RandomWord


# max_word_size cannot be negative number
def test1():
    rw = RandomWord(max_word_size=-15, constant_word_size=True)
    assert rw.generate() is None


# max_word_size=0
def test2():
    rw = RandomWord(max_word_size=0, constant_word_size=True)
    assert rw.generate() is None


# Large max_word_size generation
def test3():
    rw = RandomWord(max_word_size=1000000, constant_word_size=True)
    assert len(rw.generate()) == 1000000


def test4():
    rw = RandomWord(max_word_size=1000, constant_word_size=True)
    assert len(rw.getList(num_of_words=12)) == 12


def test5():
    rw = RandomWord(max_word_size=1000, constant_word_size=False)
    assert len(rw.getList(num_of_words=15)) == 15


def test6():
    rw = RandomWord(max_word_size=1000, constant_word_size=False)
    assert len(rw.getList(num_of_words=1000)) == 1000


def test7():
    rw = RandomWord(max_word_size=1000, constant_word_size=False)
    assert rw.getList(num_of_words=0) is None


def test8():
    rw = RandomWord(max_word_size=1000, constant_word_size=False)
    assert rw.getList(num_of_words=-15) is None


def test9():
    rw = RandomWord(max_word_size=20, constant_word_size=True,
                    special_chars="@^#\\\23", include_special_chars=True)
    assert len(rw.getList(12)) == 12
