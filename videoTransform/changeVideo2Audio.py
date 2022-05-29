from moviepy.editor import *


# 主函数
def main():
    video = VideoFileClip('test1.flv')
    audio = video.audio
    audio.write_audiofile('test1.wav')


# 主程序入口
if __name__ == '__main__':
    main()
