from flask_restful import Resource
from flask import request

# 模拟一个简单的数据库
videos = [
    {"id": 1, "title": "视频1", "url": "http://example.com/video1"},
    {"id": 2, "title": "视频2", "url": "http://example.com/video2"},
]


# 视频资源类
class Video(Resource):
    def get(self, video_id):
        video = next((video for video in videos if video["id"] == video_id), None)
        if video is None:
            return {"error": "视频未找到"}, 404
        return video

    def delete(self, video_id):
        global videos
        videos = [video for video in videos if video["id"] != video_id]
        return {"message": "视频已删除"}, 200

    def put(self, video_id):
        video = next((video for video in videos if video["id"] == video_id), None)
        if video is None:
            return {"error": "视频未找到"}, 404
        data = request.json
        video["title"] = data["title"]
        video["url"] = data["url"]
        return video


# 视频列表资源类
class VideoList(Resource):
    def get(self):
        return videos

    def post(self):
        data = request.json
        new_video = {"id": len(videos) + 1, "title": data["title"], "url": data["url"]}
        videos.append(new_video)
        return new_video, 201
