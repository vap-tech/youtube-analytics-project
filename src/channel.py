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

    @property
    def channel_id(self):
        return self.channel['items'][0]['id']

    @property
    def url(self):
        return f"https://www.youtube.com/channel/{self.channel_id}"

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)  # объект для работы с API

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, filename):
        with open(filename, 'w', encoding='utf8') as file:
            json.dump(self.channel, file, indent=2, ensure_ascii=False)

