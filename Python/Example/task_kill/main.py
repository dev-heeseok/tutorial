"""
config.ini 에 [TASK_KILL] 에 포함된 process 들을 종료 시키기 위한 프로그램입니다.

ex) config.ini 
[TASK_KILL]
TASK_NAME=TASK_NAME.exe
"""
import configparser
import psutil


def proc_kill(tasks):
    try:
        for proc in psutil.process_iter():
            if proc.name() not in tasks:
                continue

            parent = psutil.Process(proc.pid)
            for child in parent.children(recursive=True):
                print("{} kill...".format(child.name()))
                child.kill()

            print("{} kill...".format(proc.name()))
            proc.kill()
    except:
        print("throw exception...")

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    section_find = 'TASK_KILL'
    tasks = []

    sections = config.sections()    
    if section_find in sections:
        for key, val in config[section_find].items():
            tasks.append(val)
    
    if tasks:
        proc_kill(set(tasks))
    else:
        print("Task Empty")


if __name__ == '__main__':
    main()