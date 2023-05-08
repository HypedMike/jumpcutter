from moviepy.editor import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from moviepy.editor import VideoFileClip

from lib.MainVideo import MainVideo

def getSeconds(timestamp):
    timestamp = timestamp.split(":");
    seconds = int(timestamp[0]) * 60 * 60 + int(timestamp[1]) * 60 + int(timestamp[2]);
    return seconds;

def getRangesList(textfile):
    timestamps = open(textfile, "r").readlines();
    results = [];
    for i in (0, len(timestamps)):
        timing = timestamps[i].split(" ")[0];
        method = timestamps[i].split(" ")[1];
        results.append(
            (
                getSeconds(timing.split("-")[0]),
                getSeconds(timing.split("-")[1]),
                method
            )
        )
    return results;


Tk().withdraw();
filename = askopenfilename();
print("Selected file: " + filename);

textfile = askopenfilename();
print("Selected file: " + textfile);

# raw video
video = VideoFileClip(filename);

# abstract class with all the cuts
product = MainVideo("Podcast", video);

# construction of the abstract class
for timestamp in getRangesList(textfile):
    start, end, mode, name = timestamp.split(" ");
    
    if name == None or name == "":
        name = f"Clip{start}-{end}";

    start = int(start);
    end = int(end);
    if(mode == "o"):
        product.add(video.subclip(start, end));
    elif(mode == "i"):
        product.add(video.subclip(start,  end), highlight=True, title=name);



# export subclips
MainVideo.render(True);