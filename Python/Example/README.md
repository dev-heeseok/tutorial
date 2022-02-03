# Example

Document Python Example

## Index

- [logging module](#logging-module)
- [file stream module](#file-stream-module)
- [task kill module](#task-kill-module)

## logging module

**logging** 은 built-in module 이다. Python 에서는 event 를 추적하기 위해 Log message 를 출력하여 event 를 분석한다.

[logging 샘플](.\logging.py)

## file stream module

Python 에서는 File 을 Handling 하기 위해 다양한 Utility 를 지원하고 있다. 특히 **shutil module** 은 File copy, move 등 쉽게 사용할 수 있도록 기능을 지원해 주고 있다.

[file stream 샘플](.\file.py)

## task kill module

파이썬을 이용한 프로세스 종료 기능입니다.

해당 코드를 사용하기 위해서는 pip 를 이용하여 모듈을 다운받은 후 파이썬을 실행하면 된다.

```sh
# import configparser 모듈 설치
pip install configparser 

# import psutil 모듈 설치
pip install psutil
```

[task kill 샘플](.\task_kill\main.py)
