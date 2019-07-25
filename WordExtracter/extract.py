import pandas as pd
from collections import *
from pathlib import Path
import re

frequency_list = []
word_dict = dict()

for chapter_string in range(101,34886,101):
    idf = pd.read_csv('./chapter/chapters_{}.csv'.format(chapter_string), sep=',')
    column_def = idf['content']

    print('read file : ./chapter/chapters_{}.csv'.format(chapter_string))

    for i in column_def:
        # t = re.split(
        #     r'[^a-zA-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚĂĐĨŨƠàáâãèéêìíòóôõùúăđĩũơƯẠẢẤẦẨẪẬẮẰẲẴẶẸẺẼỀỂưạảấầẩẫậắằẳẵặẹẻẽếềểỄỆỈỊỌỎỐỒỔỖỘỚỜỞỠỢỤỦỨỪễệỉịọỏốồổỗộớờởỡợụủứừỬỮỰỲỴÝỶỸửữựỳỵỷỹ]'
        #     , str(i))
        # print(t)

        t = re.split(r'[^a-zA-Z\u00C0-\u024F\u1E00-\u1EFF]', str(i))

        # t = re.split(r'[ ”`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?]', str(i))
        for k, v in Counter(t).items():
            word_dict.update({k: v})
            # break
    # break


for k, v in word_dict.items():
    temp_dict = {'word': k, 'frequency': v}
    frequency_list.append(temp_dict)

output = sorted(frequency_list, key=lambda x: x['frequency'], reverse=True)
print('word indexed : {}'.format(len(output)))

odf = pd.DataFrame.from_dict(output)

file_path = Path('./WordFrequency/frequency.csv')
odf.to_csv(file_path, index=False, columns=['word', 'frequency'])