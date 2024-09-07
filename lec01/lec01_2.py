#1-100까지 짝수의 합 구하기

from lec01.lec01_1 import is_even

def main():
    total =0

    for i in range(1,100):
        if is_even(i):
            total += i
    print(f"1부터 100까지 짝수의 합은 {total}입니다")

if __name__=='__main__':
    main()