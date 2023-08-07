import argparse

from megafon_numbers_parser.numbers_request import NumbersRequest


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('maxNumbers',
                        help='Maximum count of different digits in phone number',
                        choices=range(1, 10),
                        type=int)
    args = parser.parse_args()

    numbersParser = NumbersRequest('https://nn.shop.megafon.ru/public-api/number-selection/fullnumber')
    phones = numbersParser.obtain()

    result = []
    for phone in phones:
        uniqueNumbers = set(phone)
        if len(uniqueNumbers) <= args.maxNumbers:
            result.append(phone)

    print(result)


if __name__ == '__main__':
    run()
