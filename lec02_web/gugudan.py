def main():
     dan =5
     print('구구단을 출력합니다')
     with open('leco2_html.html',"w") as f:
          f.write("<html>\n")
          for j in range(1,10):
              f.write(f"<tr><td>{dan} X {j}={dan*j}</td></tr>\n")
     print("<\html>\n")


if __name__== "__main__":
     main()