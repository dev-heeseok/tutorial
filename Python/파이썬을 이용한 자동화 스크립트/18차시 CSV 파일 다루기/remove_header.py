import os
import csv

def save_and_remove_header(file_name):
    # csv ������ �о� ����� �����ϰ� ����

    csv_rows = []

    # csv ����Ʈ ����
    with open(os.path.join('baseball-master', 'core', file_name), 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            if reader.line_num == 1:
                continue # ����� ��ŵ
            csv_rows.append(row)

    # csv ����Ʈ ����
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

    