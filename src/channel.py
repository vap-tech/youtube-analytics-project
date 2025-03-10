import os
import json

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API_KEY')  # Получаем токен
    yt = build('youtube', 'v3', developerKey=api_key)  # спец. объект для работы с API

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        yt = self.get_service()
        self.channel = yt.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.video_count = int(self.channel['items'][0]['statistics']['videoCount'])
        self.description = self.channel['items'][0]['snippet']['description']
        self.subscriber_count = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.view_count = int(self.channel['items'][0]['statistics']['viewCount'])

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    @property
    def channel_id(self):
        return self.channel['items'][0]['id']

    @property
    def url(self):
        return f"https://www.youtube.com/channel/{self.channel_id}"

    @classmethod
    def get_service(cls):
        return cls.yt  # объект для работы с API

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, filename):
        with open(filename, 'w', encoding='utf8') as file:
            json.dump(self.channel, file, indent=2, ensure_ascii=False)

