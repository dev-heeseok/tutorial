"""
과제3) 아래 코드는 자막 파일을 읽어 순번과 타이밍 정보를 제외하고 자막 내용만 별도의 텍스트 파일로 저장하는 코드의 일부이다.
첨부파일로 제공된 subtitles.zip 파일을 현재 작업디렉토리에 압출을 풀어 디렉토리 내의 모든 자막파일을 순회하여 작업을 처리하세요.

1.	대상 디렉토리를 기준으로 모든 하위 디렉토리를 함수 중에 os.walk() 함수가 있다. walk() 함수를 사용하는 사례와 동작방식에 대해서 기술하세요.

os.walk() 함수를 사용하는 사례는 `def main():` 에 정의해 두었습니다. walk 함수는 target directory 에 포함되어 있는 모든 folder 와 file 들을 가지고 올 수 있는 함수입니다. - 하위에 있는 모든 폴더 포함 -

2.	자막파일의 순번라인과 타이밍정보를 포함한 라인을 식별하기 위해 정규식을 사용할 수 있다. 순번라인을 식별하는 정규식과 타이밍정보 라인을 식별하는 정규식을 각각 re.compile() 의 인자로 들어갈 수 있게 로우(raw) 스트링으로 작성하세요.

3.	아래 코드를 참조하여 자막파일에서 자막내용만을 추출하여 다시 파일로 쓰는 코드를 완성하세요. 단, 자막파일과 같은 경로에 자막내용만 추출된 파일을 자막파일명.txt 로 저장하세요.

"""

import re
import os

def clear_dir(target_dir):
    for path, folders, files in os.walk(target_dir):
        # print('path name: ' + path)

        for file in files:
            if file.endswith('.txt'):
                os.remove(os.path.join(path, file))

    print('clear_dir done')


def get_subtitle(file_name):
    sub_title_content = []

    regex_no = re.compile(r'[\D]+')
    regex_time = re.compile(r'\d+:\d+:\d+,\d+ --> \d+:\d+:\d+,\d+')

    file = open(file_name, newline='', encoding='utf-8')

    for line in file:        
        new_line = line.strip(' \t\n\r')

        res_no = regex_no.search(new_line)
        if res_no == None:
            continue
        
        res_time = regex_time.search(new_line)
        if res_time != None:
            continue

        sub_title_content.append(new_line)

    file.close()

    return sub_title_content


def make_file_and_save(content, file_name, ext='txt'):
    file = open(file_name + '.' + ext, 'a', newline='', encoding='utf-8')

    for line in content:
        if line == '':
            continue

        file.write('%s\n' % line)

    file.close()


def main():
    target_dir = '.\Intro to Data Analysis Subtitles'
    print('current directory: ' + os.getcwd())
    print('target directory: ' + target_dir)

    # remove *.txt file
    clear_dir(target_dir)

    # execute
    for path, folders, files in os.walk(target_dir):
        print('path name: ' + path)
        
        for folder in folders:
            # print('folder name: ' + folder)
            pass

        for file in files:
            # print('file name: ' + file)
            
            file_path = os.path.join(path, file)
            subtitle_content = get_subtitle(file_path)
            make_file_and_save(subtitle_content, file_path, 'txt')


    print('job completed..')


if __name__ == '__main__':
    main()

