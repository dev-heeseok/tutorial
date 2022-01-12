import os
import csv

def save_and_remove_header(file_name):
    # csv 파일을 읽어 헤더를 제거하고 저장

    csv_rows = []

    # csv 리스트 생성
    with open(os.path.join('baseball-master', 'core', file_name), 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if reader.line_num == 1:
                continue # 헤더는 스킵
            csv_rows.append(row)

    # csv 리스트 저장
    with open(os.path.join('baseball-master', 'header-removed', file_name), 'w', newline='') as file:
        writer = csv.writer(file)

        for row in csv_rows:
            writer.writerow(row)


def main():
    os.makedirs(os.path.join('baseball-master', 'header-removed'), exist_ok=True)

    for file_name in os.listdir(os.path.join('baseball-master', 'core')):
        if not file_name.endswith('.csv'):
            continue


if __name__ == '__main__':
    main()

    