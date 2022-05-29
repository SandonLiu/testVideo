from pydub import AudioSegment
from pydub.utils import make_chunks

myaudio = AudioSegment.from_file("test1.wav", "wav")
chunk_length_ms = 29000  # 分块的毫秒数
chunks = make_chunks(myaudio, chunk_length_ms)  # 将文件切割成1秒每块

# 保存切割的音频到文件

for i, chunk in enumerate(chunks):
    # chunk_name = "test{0}.wav".format(i + 1)
    format_i = str(i + 1).rjust(3, '0')  # 001,002...010...100
    chunk_name = "test{0}.wav".format(format_i)
    print
    "exporting", chunk_name
    chunk.export(chunk_name, format="wav")

# https://blog.hepeichao.com/410.html
