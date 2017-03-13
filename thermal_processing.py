import skvideo.io
import skvideo.datasets
import os 

video = skvideo.io.vreader("FLIR0002.mp4")

def which(program):
    import os
    def is_exe(fpath):
        print("file path: " + fpath)
        print("is file: " + str(os.path.isfile(fpath)))
        print("access: " + str(os.access(fpath, os.X_OK)))
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            #print("path: " + path)
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            #print("exe file:  " + exe_file)
            if is_exe(exe_file):
                return exe_file

    return None

#ffmpeg_path = which("ffprobe.exe")
#print(os.path.split("ffprobe"))

#fpath = "C:/Users/Alyssa/Downloads/ffmpeg-3.2.2-win64-static/bin/ffprobe.exe"
#print("is file: " + str(os.path.isfile(fpath)))
#print("access: " + str(os.access(fpath, os.X_OK)))

for frame in video:
    print(frame.shape)

