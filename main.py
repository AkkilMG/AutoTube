# (c) 2022-2023, Akkil MG
# License: GNU General Public License v3.0

import asyncio
import time
from helpers import browser, gemini, convertor, youtubeUploadVideo

async def main():
    print('------------------- Testing -------------------')
    print('----------------------- Service Started -----------------------')
    try:
        # while True:
        chrome = await browser()
        print(chrome)
        if not chrome['success']:
            print('Browser failed to open')
            return
        driver = chrome['driver']
        print('+++++++++++++++ Browser opened +++++++++++++++')
        
        # data = {
        #     'title': 'Test Video',
        #     'file': "./files/test/test.mp4"
        # }
        # text = await convertor(data)
        # if not text['success']:
        #     print('Failed to convert video to text')
        #     return
        # print(text['text'])

        print('+++++++++++++++ GEMINI OPENED +++++++++++++++')
        gem = await gemini("Hello song Academy of English today we are doing a video about 10 interesting facts about the English language so fact one the longest word in English has 45 letters Heritage and I am sorry but I'm not going to try to pronounce the meaning is it is a type of language 45 lattice sentence the quick brown fox jumps over the lazy dog well this sentence using every letter of the alphabet you can see every letter of the alphabet is in this sentence for keyboard Samsung and this type of sentence is called a program this is the shortest complete sentence in the English language two words subject and this is allowed as Samsung because it is in fact A linking verb and therefore it is not take a direct object that is why this sentence example of this sentence with the contents of E is the most commonly used letter in English in most words is the most commonly used consonants and just for information the second most commonly used consonants is the latency English words begin with the letter S and any other laptop beginning of the word in English song words number seven reason the meaning of this word is it is a strong person of sounds and is often used in music and this word written it is the longest English word without a real values in this word Rhythm so an example sentence with the word reason this is a special word because it is the only English word with five consecutive vowels you you know one after the other word in English in line there is an alternative spelling with only for girls of these spellings is variations of the spelling the architect the same word let's look at an example in the museum King to go into the Museum so they are waiting in line 7 different ways to pronounce the following classes this combination of four letters is very common in English and seven ways to pronounce depending on the on the word love true transcription here this is the pronunciation pronunciation") #text['text'])
        if not gem['success']:
            print('Failed to login to GEMINI')
            return
        print('+++++++++++++++ GEMINI CLOSED +++++++++++++++')

        yt = await youtubeUploadVideo(driver, gem['data'])
        if not yt['success']:
            print('Failed to upload video')
            return
        driver = yt.get('driver')
    except Exception as e:
        print(f"Exception occurred (main): {e}")
        return

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('----------------------- Service Stopped -----------------------')