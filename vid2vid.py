import os
import cv2
import torch
import folder_paths
import numpy as np
from PIL import Image, ImageOps

input_path = folder_paths.get_input_directory()
out_path = folder_paths.get_output_directory()

class LoadVideo:
    @classmethod
    def INPUT_TYPES(s):
        files = [f for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f)) and f.split('.')[-1] in ["mp4", "webm","mkv","avi"]]
        return {"required":{
            "video":(files,),
        }}

    ## Info ##
    CATEGORY = "VID2VID"
    DESCRIPTION = "Loads a Video File."
    OUTPUT_NODE = False

    ## Func ##
    RETURN_TYPES = ("VIDEO",)
    FUNCTION = "load_video"

    def load_video(self, video):
        video_path = os.path.join(input_path,video)
        return (video_path,)

class SaveVideo:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"Video": ("Video", {"tooltip": "The Video to get Extracted."}), }}

    ## Info ##
    CATEGORY = "VID2VID"
    DESCRIPTION = "Saves a Video File."
    OUTPUT_NODE = True

    ## Func ##
    RETURN_TYPES = ()
    FUNCTION = "save_video"

    def save_video(self, Video):
        file = open(os.path.join(out_path, "output_video.mp4"), "rb")
        return (file)

class Img2VideoConvertor:       
    @classmethod    
    def INPUT_TYPES(s):
        return { "required": {"IMAGE": ("IMAGE", {"tooltip": "The Images to get converted back into a Video."}), }}
    
    ## Info ##
    CATEGORY = "VID2VID/convertor"    
    DESCRIPTION = "Converts the jpg Sequences into a Video."
    OUTPUT_NODE = False
    
    ## Func ##
    RETURN_TYPES = ("Video",)
    FUNCTION = "convert_img2vid"
    
    def convert_img2vid(self, IMAGE):
        
        
        Video
        return (Video, )

class Video2ImgConvertor:       
    @classmethod    
    def INPUT_TYPES(s):
        return { "required": {"Video": ("VIDEO", {"tooltip": "The Video to get Extracted."}), }}
    
    ## Info ##
    CATEGORY = "VID2VID/convertor"    
    DESCRIPTION = "Converts the Video into jpg Sequences."
    OUTPUT_NODE = False
    
    ## Func ##
    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "convert_vid2img"
    
    def convert_vid2img(self, Video):
        vidcap = cv2.VideoCapture(filename=str(Video))
        success,image = vidcap.read()
        images = []
        count = 0
        while success:
            images.append(image)
            success,image = vidcap.read()
            count += 1
        
        
        if len(images.shape) == 5:
                image = images.reshape(-1, images.shape[-3], images.shape[-2], images.shape[-1])
        return (images, )