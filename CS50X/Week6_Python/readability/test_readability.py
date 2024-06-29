from readability import check_grade


def test_check_grade():
    txt = "One fish. Two fish. Red fish. Blue fish."
    assert check_grade(txt) <= 1

def test_check_grade2():
    txt = "Would you like them here or there? I would not like them here or there. I would not like them anywhere."
    assert check_grade(txt) == 2

def test_check_grade3():
    txt = "Congratulations! Today is your day. You're off to Great Places! You're off and away!"
    assert check_grade(txt) == 3

def test_check_grade4():
    txt = "Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard."
    assert check_grade(txt) == 5

def test_check_grade5():
    txt = "In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since."
    assert check_grade(txt) == 7

def test_check_grade6():
    txt = "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversation?'"
    assert check_grade(txt) == 8

def test_check_grade7():
    txt = "There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy."
    assert check_grade(txt) == 9

def test_check_grade8():
    txt = "It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."
    assert check_grade(txt) == 10

def test_check_grade9():
    txt = "A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains."
    assert check_grade(txt) >= 16


