from src.video import Video, PLVideo


def test_video():
    vl = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
    assert vl.video_url == 'https://youtu.be/4fObz_qw9u4'
    assert vl.__str__() == 'MoscowPython Meetup 78 - вступление'


def test_error():
    vl2 = Video('broken_id')
    assert vl2.title is None
    assert vl2.like_count is None
    assert vl2.view_count is None
