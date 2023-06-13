from src.channel import Channel
from datetime import timedelta
import isodate


class PlayList:
    yt = Channel.get_service()

    def __init__(self, pl_id):
        self.__id = pl_id

        data = self.yt.playlists().list(id=pl_id,
                                        part='snippet',
                                        ).execute()
        self.title = data["items"][0]["snippet"]["title"]

        data = self.yt.playlistItems().list(playlistId=self.__id,
                                            part='contentDetails',
                                            maxResults=50,
                                            ).execute()
        self.__items_id = [i['contentDetails']['videoId'] for i in data['items']]

        self.__total_duration = self.get_total_duration()

    def get_total_duration(self):
        videos = self.yt.videos().list(part='contentDetails,statistics',
                                       id=','.join(self.__items_id)
                                       ).execute()

        durations = timedelta()

        for video in videos['items']:
            iso_8601_duration = video['contentDetails']['duration']
            durations += isodate.parse_duration(iso_8601_duration)

        return durations

    @property
    def total_duration(self):
        return self.__total_duration

    @property
    def url(self):
        return f'https://www.youtube.com/playlist?list={self.__id}'

    def show_best_video(self):
        videos = self.yt.videos().list(part='statistics',
                                       id=','.join(self.__items_id)
                                       ).execute()
        count_like = 0
        video_id = ''

        for item in videos['items']:
            count_like_item = int(item['statistics']['likeCount'])
            if count_like_item > count_like:
                count_like = count_like_item
                video_id = item['id']

        return f'https://youtu.be/{video_id}'
