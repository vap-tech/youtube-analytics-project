from src.playlist import PlayList
import datetime


def test_playlist():
    pl = PlayList('PLH-XmS0lSi_zdhYvcwUfv0N88LQRt6UZn')
    assert pl.title == "Лучшие доклады Saint HighLoad++ 2022"
    assert pl.url == "https://www.youtube.com/playlist?list=PLH-XmS0lSi_zdhYvcwUfv0N88LQRt6UZn"

    duration = pl.total_duration
    assert str(duration) == "12:19:26"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 44366.0

    assert pl.show_best_video() == "https://youtu.be/iixB6Yo4G5I"
