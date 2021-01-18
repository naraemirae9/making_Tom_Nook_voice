from gtts import gTTS
from pydub import AudioSegment
import random, os

#directory 만들기
os.makedirs('samples', exist_ok=True)
os.makedirs('result', exist_ok=True)

string ='일어났니 동숲하자'
lang = 'ko'
random_factor = 0.35 #옥타브 변경
normal_frame_rate=44100

#오디오 변형
result_sound =None

for i, letter in enumerate(string):
    if letter == ' ': #sound가 공백인 경우
        new_sound = letter_sound._spawn(b'\x00' * (normal_frame_rate // 3), overrides={'frame_rate':normal_frame_rate})

    else: #sound가 공백이 아닌 경우
        if not os.path.isfile('/Users/youmirae/samples/%s.mp3'%letter): #이미 있는지 체크
            tts = gTTS(letter, lang=lang)
            tts.save('/Users/youmirae/samples/%s.mp3'%letter)


        #sample sound 로드
        letter_sound = AudioSegment.from_mp3('/Users/youmirae/samples/%s.mp3' % letter)

        #처음과 끝부분 공백 삭제
        raw = letter_sound.raw_data[5000:-5000]

        #음정 조절
        octaves =2.0 + random.random() * random_factor
        frame_rate= int(letter_sound.frame_rate * (2.0 ** octaves))
        print('%s - octaves: %.2f, fr: %.d' % (letter, octaves,frame_rate))

        new_sound=letter_sound._spawn(raw, overrides={'frame_rate': frame_rate})

    new_sound = new_sound.set_frame_rate(normal_frame_rate)
    result_sound=new_sound if result_sound is None else result_sound + new_sound

result_sound

result_sound.export('/Users/youmirae/result/%s.mp3' % string, format='mp3')



    


        
