import pytest
from unittest import mock  # імпортуємо мокк для #20
from file_helper import Api, FileHelper
import os

# 13 створюємо фікстуру:
@pytest.fixture
def temp_file(tmp_path):  # створюємо якийсь файл
    f = tmp_path / 'filename.txt'
    f.write_text('SOME CONTENT')  # записали в файл якийсь текст
    return f  # повертаємо цей файл

# 18 створюємо фікстуру api
@pytest.fixture
def api():
    api =  Api('api_key_secret')
    yield api
    api.close()

# 15 створюємо нову фікстуру, щоб уникнути повторення коду в #12 і #14:
@pytest.fixture
def fh(api):
    fh = FileHelper(api)
    return fh

# -------------------------------------------------------------------------------------------
# 12 створюємо клас TestFileHelper:
class Test_FileHelper:
    def test_init(self):  # - тест для api
        api = object()  # 12.1
        fh = FileHelper(api)  # 12.2
        assert fh.api is api

# 14 перевірємо що створений файл дійсно видаляється
    def test_remove_file(self, temp_file):
        api = object()  # 14.1
        fh = FileHelper(api)  # 14.2
        fh.remove_file(temp_file)  # тут видаляємо створений файл і
        assert os.path.exists(temp_file) is False  # перевіряємо, що він більше не існує
# -------------------------------------------------------------------------------------------

# 16 так як 12.1+12.2 і 14.1+14.2 повторюються, створимо нову фікстуру #15
class Test_FileHelper2:
    def test_init(self):  # - тест для api
        api = object()
        fh = FileHelper(api)
        assert fh.api is api

# тут код вже без api і fh(їх перенесено до фіксутри def temp_file(tmp_path)):
    def test_remove_file(self, fh, temp_file):
        fh.remove_file(temp_file)  # тут видаляємо створений файл і
        assert os.path.exists(temp_file) is False  # перевіряємо, що він більше не існує

# 20 створюємо тест на upload_file:
    @mock.patch.object(FileHelper, 'prepare_file', autospec=True)
    def test_upload_file(self, mocked_prepare_file):
        fake_api = mock.MagicMock()
        # expected_data = object()
        # mocked_prepare_file.return_value = expected_data
        fake_filepath = 'some_some'
        fh = FileHelper(fake_api)
        fh.upload_file(fake_filepath)
        fake_api.request.assert_called_once_with('POST', mocked_prepare_file.return_value,)
        mocked_prepare_file.assert_called_once_with(
            fh,
            fake_filepath,
        )
