#홀짝구분하기

def is_even(n):
    return n%2==0

def main():
    n=int(input('숫자를 입력하시오'))

    if n %2 ==0:
        print(f'{n}은 짝수입니다')

    else:
        print(f"{n}은 홀수입니다")

if __name__=='__main__':
    main()