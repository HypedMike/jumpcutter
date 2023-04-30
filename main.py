from moviepy.editor import *
from tkinter import *
from tkinter.filedialog import askopenfilename
from moviepy.editor import VideoFileClip

def getSeconds(timestamp):
    timestamp = timestamp.split(":");
    seconds = int(timestamp[0]) * 60 * 60 + int(timestamp[1]) * 60 + int(timestamp[2]);
    return seconds;

def getRangesList(textfile):
    timestamps = open(textfile, "r").readlines();
    results = [];
    for i in (0, len(timestamps)):
        print(timestamps[i]);
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

video = VideoFileClip(filename);


subclips = [];
actualvideo = [];

print(getRangesList(textfile));
exit();

for timestamp in getRangesList(textfile):
    start, end, mode = timestamp.split(" ");
    start = int(start);
    end = int(end);
    if(mode == "o"):
        actualvideo.append(video.subclip(start, end));
    elif(mode == "i"):
        subclips.append(video.subclip(start, end));



# export subclips
n = 0;
for sc in subclips:
    sc.write_videofile("highlight" + str(n) + ".mp4", fps=30);
    n = n + 1;

# export main video
finalvideo = concatenate_videoclips(actualvideo);
finalvideo.write_videofile("finalvideo.mp4", fps=30);