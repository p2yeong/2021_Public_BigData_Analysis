from pydub import AudioSegment
from pydub.utils import make_chunks

folder = "C:\\Users\\EunYeong\\PycharmProjects\\deepAsmr\\asmr_youtube\\asmr_rainy\\"
file = 'rain_in_the_forest.wav'
myaudio = AudioSegment.from_file(folder + '/' + file, "wav")
chunk_length_ms = 1000*30 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

#Export all of the individual chunks as wav files

for i, chunk in enumerate(chunks):
    chunk_name = "rain_sound{0}.wav".format(i)
    print("exporting", chunk_name)
    chunk.export(chunk_name, format="wav")



import os
from moviepy.editor import *
def mp4_to_wav():
    # os.chdir("C:/Users/EunYeong/Downloads/asmr_datakr/")
    os.chdir("C:\\Users\\EunYeong\\PycharmProjects\\deepAsmr\\asmr_youtube\\asmr_rainy\\")
    videos = os.listdir()
    for video in videos:
        clip = AudioFileClip(video)
        name = ''.join(video.split('.')[:-1])
        clip.write_audiofile(f"{name}.wav", 44100, 2, 2000, "pcm_s32le")
        # filename, frames per second, Sample width (set to 2 for 16-bit sound), buffersize, codec ( ‘pcm_s32le’ for 32-bit wav)
    print("파일 변환 완료")
os.getcwd()

mp4_to_wav()