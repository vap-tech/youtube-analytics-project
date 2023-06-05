from src.channel import Channel


def test_channel():
    """Тестируем класс Channel"""
    ch = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    assert ch.channel_id == 'UC-OVMPlMA3-YCIeg4z5z23A'
    assert ch.url == 'https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A'
    ch.print_info()
    ch.to_json('test.json')

    # tests to homework 3
    ch2 = Channel('UCwHL6WHUarjGfUM_586me8w')
    assert str(ch) == 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'
    assert (ch + ch2) > 100000
    assert (ch - ch2) < -46300
    assert (ch2 - ch) > 48300
    assert not (ch > ch2)
    assert not (ch >= ch2)
    assert (ch < ch2)
    assert (ch <= ch2)
    assert not (ch == ch2)
