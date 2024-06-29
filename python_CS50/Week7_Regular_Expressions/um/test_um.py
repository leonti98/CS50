from um import count


def test_count_just_um():
    assert count("um") == 1


def test_count_question():
    assert count("um?") == 1


def test_count_start_coma():
    assert count("Um, thanks for the album.") == 1


def test_count_end_dots():
    assert count("Um, thanks, um...") == 2


def test_count_dots():
    assert count("um...") == 1


def test_count_midde_coma():
    assert count("hello, um, world") == 1


def test_count_two_coma():
    assert count("um, hello, um, world ") == 2


def test_count_yum():
    assert count("yum") == 0


def test_count_all_in_one():
    assert (
        count(
            "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?"
        )
        == 2
    )
