#!/usr/bin/python3
import argparse, subprocess, datetime

parser = argparse.ArgumentParser(description='Concatenate mp4 files')
parser.add_argument('clips', metavar='video', nargs='+',
                    help='path to video')
parser.add_argument('-u', '--unsorted', action='store_true',
                    help='use to disable sorting by name')

files=parser.parse_args().clips
us=parser.parse_args().unsorted

if not us: files=sorted(files)

with open("list", "w") as f:
    for file in files:
        f.write(f"file '{file}'\n")

date=datetime.datetime.strftime(datetime.datetime.now(), "%m.%d-%H.%M")
subprocess.call(f"ffmpeg -f concat -safe 0 -i list -c copy {date}.mp4")

