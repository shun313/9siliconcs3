birth_year = int(input("Please enter your birth year: "))

if birth_year < 1900:
    print("That is a invalid Year, it should not be earlier than 1900")
else:
    zodiac = ["Rat (鼠 / Shǔ)","Ox (牛 / Niú)","Tiger (虎 / Hǔ)","Rabbit (兔 / Tù)","Dragon (龙 / Lóng)","Snake (蛇 / Shé)","Horse (马 / Mǎ)","Goat (羊 / Yáng)","Monkey (猴 / Hóu)","Rooster (鸡 / Jī)","Dog (狗 / Gǒu)","Pig (猪 / Zhū)"]

    index = (birth_year - 1900) % 12
    print(f"Congrats! Your Chinese Zodiac Sign is {zodiac[index]}!")

<img width="1875" height="178" alt="image" src="https://github.com/user-attachments/assets/328d733d-4a6a-4bd6-8658-787c833752d3" />
<img width="740" height="92" alt="image" src="https://github.com/user-attachments/assets/1ea4cad4-f741-41de-bdde-0d6f0b982c3c" />
