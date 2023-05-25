def z1():
    import re
    import random

    def read_synonyms(file_path):
        synonyms = {}
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(' - ')
                if len(parts) < 2:
                    continue
                word = parts[0]
                syns = [syn.strip() for syn in parts[1].split(';')]
                synonyms[word] = syns
        return synonyms

    def replace_synonym(word, synonyms):
        if word in synonyms:
            available_synonyms = synonyms[word]
            if available_synonyms:
                synonym = random.choice(available_synonyms)
                print(f"Заменить '{word}' на синоним '{synonym}'?")
                choice = input("Введите 'да' или 'нет': ")
                if choice.lower() == 'да':
                    return synonym
        return word

    def add_synonym(file_path, word, synonym):
        with open(file_path, 'a') as file:
            file.write(f"\n{word} - {synonym};")

    def main():
        synonyms_file = "synonyms.txt"
        synonyms = read_synonyms(synonyms_file)

        sen = input("Введите слово: ")
        words = sen.split()

        new_sen = ""
        for word in words:
            new_word = replace_synonym(word, synonyms)
            if new_word == word:
                print(f"Не найдено синонима для слова '{word}'.")
                choice = input("Введите свой синоним или 'пропустить': ")
                if choice.lower() != 'пропустить':
                    add_synonym(synonyms_file, word, choice)
                    new_word = choice
            new_sen += new_word + " "

        print("Измененное слово:", new_sen)

    if __name__ == "__main__":
        main()

def z2():
    from pydub import AudioSegment
    import pydub

    pydub.AudioSegment.converter = 'D:\dop zadachi\ljg kf,s.exe'
    f = AudioSegment.from_wav("D:\dop zadachi\ljg kf,s\muz.wav")

    def speed_change(sound, speed=1.0):
        s = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
        return s.set_frame_rate(sound.frame_rate)

    i = input('Введите значение замедления: ')

    fast = speed_change(f, float(i))

    fast.export("новаяверсия.wav", format="wav")

def z3():
    from functools import reduce

    def reduce_fun(prev, tec):
        if tec[0] > prev[0]:
            print(tec[0], ' '.join(tec[1]))
            return tec
        else:
            return prev

    f = open('news.txt', 'r', encoding='UTF8')
    array = []

    for line in f.readlines():
        count, *post = line.split()
        array.append([int(count), post])
    print(array[0][0], ' '.join(array[0][1]))
    reduce(reduce_fun, array)

#z1()
z2()
#z3()

