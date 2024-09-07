#단위변환

def temp_c_change(temp_f):
    temp_c=(temp_f-32)*1.8
    return temp_c

def main():
    temp_f =int(input('변환하고자하는 화씨 온도를 적으시오'))
    temp_c=temp_c_change(temp_f)

    print(f"{temp_f}℉=>{temp_c}℃")

if __name__=="__main__":
    main()

