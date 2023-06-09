from src.channel import Channel


class Video:
    yt = Channel.get_service()

    def __init__(self, video_id: str):
        """
       - id видео
       - название видео
       - ссылка на видео
       - количество просмотров
       - количество лайков
         """

        self.vr = self.yt.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                        id=video_id
                                        ).execute()
        self.id: str = self.vr['items'][0]['id']
        self.video_title: str = self.vr['items'][0]['snippet']['title']
        self.view_count: int = self.vr['items'][0]['statistics']['viewCount']
        self.like_count: int = self.vr['items'][0]['statistics']['likeCount']

    def __str__(self) -> str:
        return self.video_title

    @property
    def video_url(self) -> str:
        return f'https://youtu.be/{self.id}'


class PLVideo(Video):
    def __init__(self, video_id: str, pl_id: str):
        super().__init__(video_id)
        self.pl_id = pl_id
