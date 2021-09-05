import os

class Session:
    def close(self):
        print('Closed session')

# 19 створюємо клас Апі
class Api:
    def __init__(self, api_key):
        self.api_key = api_key
        self.session = Session()

    def request(self, method, data):
        print('Executed', method)

    def close(self):
        print('Closing session')
        self.session.close()

# 11 створили якийсь файлхелпер, для того щоб покрити його тестами:
class FileHelper:
    def __init__(self, api):
        self.api = api

    def remove_file(self, filepath):
        if os.path.isfile(filepath): # за допомогою модуля os перевіряємо чи існує такий файл (filepath)
            print(f'removing file {filepath!r})')
            os.unlink(filepath)

    def prepare_file(self, filepath):
        print(f'Preparing file {filepath!r} for upload')
        return bytes()

    def upload_file(self, filepath):
        data = self.prepare_file(filepath)
        self.api.request('POST', data)
