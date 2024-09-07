#소수구하기
from lec01.lec01_3 import is_prime

def main():
    n= []
    for num in range(0,100):
        if is_prime(num):
            n.append(num)
    print(f"{n}은 소수 입니다")


if __name__=='__main__':
    main()