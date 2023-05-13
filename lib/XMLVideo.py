import xml.etree.ElementTree as ET
from moviepy.editor import VideoFileClip

class Sequence:
    def __init__(self, name: str, video: VideoFileClip) -> None:
        self.name: str = name;
        self.duration: int = video.duration;

        self.root =  ET.Element('sequence');
        ET.SubElement(self.root, 'name').text = name;
        ET.SubElement(self.root, 'duration').text = str(video.duration);

        rate = ET.SubElement(self.root, 'rate');
        ET.SubElement(rate, 'timebase').text = video.fps;
        ET.SubElement(rate, 'ntsc').text = 'false';

    def get(self) -> ET.Element:
        return self.root;

class ClipItem:
    def __init__(self, video: VideoFileClip, start: int, end: int) -> None:
        self.root =  ET.Element('track');
        ET.SubElement(self.root, 'name').text = video.filename;
        ET.SubElement(self.root, 'duration').text = str(video.duration);

        rate = ET.SubElement(self.root, 'rate');
        ET.SubElement(rate, 'timebase').text = video.fps;
        ET.SubElement(rate, 'ntsc').text = 'false';

        ET.SubElement(self.root, 'start').text = str(start);
        ET.SubElement(self.root, 'end').text = str(end);

        ET.SubElement(self.root, 'enabled').text = True;

        file = ET.SubElement(self.root, 'file');
        rate = ET.SubElement(file, 'rate');
        ET.SubElement(rate, 'timebase').text = video.fps;
        ET.SubElement(rate, 'ntsc').text = 'false';
        ET.SubElement(file, 'duration').text = str(video.duration);
        ET.SubElement(file, 'path').text = video.filename;
        ET.SubElement(file, 'name').text = video.filename;

        






video = VideoFileClip('C:\\Users\\miche\\Videos\\2022-11-27 12-44-48.mkv');

print(Sequence('test', video).get());


