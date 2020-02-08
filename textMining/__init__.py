from textMining.ctrl import Ctrl

if __name__ == '__main__':
    def print_menu():
        print('0. exit')
        print('1. 사전 다운로드')
        print('2. 삼성 전략보고서 분석')

        return input('Select Menu\n')

    app = Ctrl()
    while 1:
        menu = print_menu()
        if menu == '1':
            app.download_Dictionary()
        if menu == '2':
            app.download_Analysis()
            print(1)
        elif menu == '0':
            break