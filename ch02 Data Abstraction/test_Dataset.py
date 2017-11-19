# test_Dataset.py
from Dataset import Dataset


def main():
    info = ('This is a program to compute the min, max, mean and\n'
            'standard deviation for a set of numbers.\n')
    print(info)
    data = Dataset()
    while True:
        xStr = input('enter a number (<Enter> to quit): ')
        if xStr == '':
            break
        try:
            x = float(xStr)
        except ValueError:
            print('Invalid Entry Ignored: Input was not a number')
            continue
        data.add(x)
    print('Summary of', data.size(), 'scores.')
    print('Min:', data.min())
    print('Max:', data.max())
    print('Mean:', data.average())
    print('Standard Deviation:', data.std_deviation())


if __name__ == '__main__':
    main()
