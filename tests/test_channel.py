from src.channel import Channel


def test_channel():
    """Тестируем класс Channel"""
    ch = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    assert ch.channel['items'][0]['id'] == 'UC-OVMPlMA3-YCIeg4z5z23A'
    ch.print_info()
