from unittest import mock
from json import JSONDecodeError

from megafon_numbers_parser.numbers_request import (NumbersRequest, NumbersUrlNotFound)


def readFile(filename):
    with open(filename, 'r') as file:
        content = file.read()

    return content


def isPhoneNumbers(numbers):
    for number in numbers:
        if not all(char.isdigit() for char in number):
            return False

    return True


def getFakeGet(statusCode, content):
    m = mock.Mock()
    m.status_code = statusCode
    m.content = content

    def getFakeContent(url, params):
        return m

    return getFakeContent


@mock.patch('requests.get', getFakeGet(404, 'Not found'))
def test_page_not_found():
    # Arrange
    numbersRequest = NumbersRequest('https://nn.shop.megafon.ru/public-api/number-selection/fullnumber')
    hasException = False
    errorMessage = ''

    # Act
    try:
        numbers = numbersRequest.obtain()
    except NumbersUrlNotFound as e:
        hasException = True
        errorMessage = e.args[0]

    # Assert
    assert 'numbers' not in locals()
    assert hasException
    assert len(errorMessage) != 0
    assert errorMessage == 'https://nn.shop.megafon.ru/public-api/number-selection/fullnumber returns 404 error code'


@mock.patch('requests.get', getFakeGet(200, readFile('tests/data/numbers.json')))
def test_parsing_numbers_is_succeeded():
    # Arrange
    numbersRequest = NumbersRequest('https://nn.shop.megafon.ru/public-api/number-selection/fullnumber')

    # Act
    numbers = numbersRequest.obtain()

    # Assert
    assert isinstance(numbers, list)
    assert all(isinstance(number, str) for number in numbers)
    assert isPhoneNumbers(numbers)


@mock.patch('requests.get', getFakeGet(200, readFile('tests/data/invalidJson.txt')))
def test_parsing_invalid_json_raise_error():
    # Arrange
    numbersRequest = NumbersRequest('https://nn.shop.megafon.ru/public-api/number-selection/fullnumber')
    hasException = False

    # Act
    try:
        numbers = numbersRequest.obtain()
    except JSONDecodeError:
        hasException = True

    # Assert
    assert 'numbers' not in locals()
    assert hasException
