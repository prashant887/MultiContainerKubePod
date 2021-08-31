import requests
import time

logFile = '/log/webout.log'
i = 0
with open(logFile, 'a') as f:
    while i <= 100:
        try:
            res = requests.get('http://localhost:8080')
            cod = res.status_code
            data = res.text
            message = "Code = {}  Data={}".format(cod, data)
            f.writelines(message)
            time.sleep(5)
        except Exception as e:
            print(e)
        i = i + 1
    f.close()
