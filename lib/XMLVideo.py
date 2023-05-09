import xml.etree.ElementTree as ET

class XMLVideo:
    def __init__(self, path) -> None:
        self.root = ET.Element("xmeml");
        self.sequence = ET.SubElement(self.root, "sequence");
        sequence_name = ET.SubElement(self.sequence, "name");
        self.media = ET.SubElement(self.sequence, "media");
        self.video = ET.SubElement(self.media, "video");
        self.track = ET.SubElement(self.video, "track");
        sequence_name.text = "My Timeline";
        self.path = path;
    
    def addSection(self, start, end, type):
        clipitem = ET.SubElement(self.track, "clipitem");
        clipitem.set("id", self.path);

        duration = ET.SubElement(clipitem, "duration");
        duration.text = str(end - start);

        rate = ET.SubElement(clipitem, "rate");
        rate.text = "24";
        ntsc = ET.SubElement(clipitem, "ntsc");
        ntsc.text = "FALSE";
    
        time_start = ET.SubElement(clipitem, "start");
        time_start.text = str(start);
    
        time_end = ET.SubElement(clipitem, "end");
        time_end.text = str(end);
    
        # file description
        file_desc = ET.SubElement(clipitem, "file");
        file_desc.set("id", self.path);
    
        pathurl = ET.SubElement(file_desc, "pathurl");
        pathurl.text = self.path;
    
    def save(self):
        tree = ET.ElementTree(self.root);
        tree.write("seq.xmeml");


xml = XMLVideo("video.mp4");
xml.save();