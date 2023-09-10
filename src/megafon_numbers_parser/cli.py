import argparse

from megafon_numbers_parser.numbers_request import NumbersRequest


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('maxNumbers',
                        help='Maximum count of different digits in phone number',
                        choices=range(1, 10),
                        type=int)
    args = parser.parse_args()

    numbersParser = NumbersRequest('https://api.shop.megafon.ru/number/356/allNumbers')
    phones = numbersParser.obtain()

    for phone in phones:
        uniqueNumbers = set(str(phone))
        if len(uniqueNumbers) <= args.maxNumbers:
            print(phone)


if __name__ == '__main__':
    run()
