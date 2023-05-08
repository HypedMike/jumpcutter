from moviepy.editor import VideoFileClip, concatenate_videoclips

class HighLight:
    def __init__(self, name: str, video) -> None:
        self.video: VideoFileClip = video;
        self.name = name;

    def render(self):
        self.video.write_videofile(f"{self.name} highlight.mp4", fps=30);

class MainVideo:
    def __init__(self, title, raw_video: VideoFileClip):
        self.list: list[VideoFileClip] = [];
        self.hllist: list[HighLight] = [];
        self.title: str = title;
        self.raw: VideoFileClip = raw_video;
    
    def add(self, video, highlight: bool = False, title: str = None):
        if(highlight == False or highlight == None):
            self.list.append(video);
        else:
            highlight = HighLight(title, video);
            self.hllist.append(video);
    
    def addIntro(self, video):
        self.list.insert(0, video);

    def render(self, all: bool = False):
        concatenate_videoclips(self.list).write_videofile(f"{self.title}.mp4");
        
        if(all):
            for video in self.hllist:
                video.render();