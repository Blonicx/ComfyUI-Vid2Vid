from .vid2vid import LoadVideo, SaveVideo, Video2ImgConvertor, Img2VideoConvertor

NODE_CLASS_MAPPINGS = {
    "LoadVideo" : LoadVideo,
    "SaveVideo" : SaveVideo,
    "Video2ImgConvertor" : Video2ImgConvertor,
    "Img2VideoConvertor" : Img2VideoConvertor,
}

__all__ = ['NODE_CLASS_MAPPINGS']