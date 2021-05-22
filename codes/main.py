import requests
import time
from multiprocessing import Process
import re
import os
import shutil
base_path = "F:\\user_setting\\Desktop\\pictures"
def read_data(begin, end, urls, index):
    for i in range(begin, end):
        time.sleep(0.3)
        response = requests.get(urls[i])
        with open("F:\\user_setting\\Desktop\\pictures\\pic_" + str(i + index) + ".jpg", "wb") as f:
            f.write(response.content)

if __name__ == '__main__':
    config = input("do you want to collect pictures from those urls(y/n)")
    if config == 'n':
        exit(0)
    urls = []
    with open("F:\\user_setting\\Desktop\\links.txt", "r") as f:
        for line in f:
            urls.append(line.strip("\n"))
    if not os.path.exists(base_path):
        os.mkdir(base_path)
    else:
        shutil.rmtree(base_path)
        os.mkdir(base_path)
    add_sum = int(len(urls) / 12)
    now = 0
    index = 0
    with open("F:\\git_message\\Resources\\img\\rank.txt", "r+") as f:
        index = int(f.read())
        f.seek(0)
        f.write(str(index + len(urls)))
    all_line = []
    with open("F:\\hexo\\wodeboke\\themes\\butterfly\\source\\js\\mychange.js", "r", encoding='utf-8') as f:
        for line in f:
            if re.search("total_picture", line):
                line = re.sub(r'total_picture = [0-9]+', "total_picture = " + str(index + len(urls) - 1), line)
            all_line += line

    with open("F:\\hexo\\wodeboke\\themes\\butterfly\\source\\js\\mychange.js", "w", encoding='utf-8') as f:
        for i in range(len(all_line)):
            f.write(all_line[i])


    for i in range(11):
        Process(target=read_data, args=(now, now+add_sum, urls, index, )).start()
        now += add_sum
    Process(target=read_data, args=(now, len(urls), urls, index, )).start()
'''import os
import re
base_path = "F:\\git_message\\Resources\\img"
all_files = os.listdir(base_path)[: -1]
all_sum = []
for file_name in all_files:
    all_sum.append(int(re.findall(r'\d+', file_name)[0]))
all_sum.sort()
loop = 0
for sum in all_sum:
    os.rename(base_path+"\\pic_" + str(sum) + ".jpg", base_path + "\\pic_" + str(loop) + ".jpg")
    loop += 1'''