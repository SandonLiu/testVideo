from aip import AipSpeech

APP_ID = '25599639'
API_KEY = '6QakL8hWFkYNHFzHxz2X9qQl'
SECRET_KEY = 'EhbVdPlGkNZNOTSQq0zkXzzNQAfKN2Yh'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# 读取文件并识别本地文件
def recognize(file_name):
    data = open(file_name, 'rb').read()
    result = client.asr(data, 'wav', 16000, {'dev_pid': 1537})
    return result


result = recognize('test002.wav')
text = result['result'][0]
print(result)
print(text)

