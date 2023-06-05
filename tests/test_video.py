from src.video import PLVideo


def test_video():
    vl = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert vl.video_url == 'https://youtu.be/4fObz_qw9u4'
    assert vl.__str__() == 'MoscowPython Meetup 78 - вступление'
