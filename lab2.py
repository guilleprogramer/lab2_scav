import os

def cut(start, time, video, new_video):
    os.system('ffmpeg -ss '+start+' -i '+video+' -c copy -t '+time+' '+new_video)

def yuv_histogram(video):
    os.system('ffplay '+video+' -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay"')

def resize(pixels, video, new_video):
    if len(pixels) == 3:
        c = 'ffmpeg -i '+video+' -filter:v scale='+pixels+':-1 -c:a copy '+new_video
    elif len(pixels) > 3:
        c = 'ffmpeg -i '+video+' -s '+pixels+' -c:a copy '+new_video
    os.system(c)

def mono(video,new_video):
    os.system('ffmpeg -i '+video+' -map_channel 0.1.0 -c:v copy '+new_video)


####---MAIN----########
#####EXERCISE 1########
#cut('40','12','BBB.mp4','new_BBB.mp4')

#####EXERCISE 2########
#yuv_histogram('BBB.mp4')

#####EXERCISE 3########
#resize('360x240', 'BBB.mp4', '360x240.mp4')

#####EXERCISE 4########
#mono('BBB.mp4','mono_BBB.mp4')