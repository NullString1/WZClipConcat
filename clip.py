#!/usr/bin/python3
import argparse, subprocess, datetime, sys

class argParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f"error: {message}\n\n")
        self.print_help()
        sys.exit(2)

parser = argParser(description="Concatenate mp4 files")
parser.add_argument("clips", metavar="video", nargs="+",
                    help="path to video")
parser.add_argument("-u", "--unsorted", action="store_true",
                    help="use to disable sorting by name")

files=parser.parse_args().clips
us=parser.parse_args().unsorted

if not us: files=sorted(files)

with open("list", "w") as f:
    for file in files:
        f.write(f"file '{file}'\n")

date=datetime.datetime.now().strftime("%m.%d-%H.%M")
subprocess.run(["ffmpeg", "-f", "concat", "-safe", "0", "-i", "list", "-c", "copy", f"{date}.mp4"])

