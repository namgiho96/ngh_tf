from titanic.ctrl import Ctrl
from titanic.view import View

if __name__ == '__main__':

    def print_menu():
        print('0. Exit')
        print('1. 시각화')
        print('2. 모델링')  # 추상화된 상태  모델링
        print('3. 머신러닝')  # 그걸 학습을 머신러님 시키고
        print('4. 머신생성')  # 셍성을한다
        return input('메뉴 입력\n')

    app = Ctrl()

    while 1:
        menu = print_menu()
        if menu == '1':
            view = View('train.csv')
            menu = input('차트 내용 선택 \n'
                         '1. 생존자 vs 사망자 \n'
                         '2. 생존자 성별 대비')
            if menu == '1':
                view.plot_survived_dead()
            if menu == '2':
                view.plot_sex()
        if menu == '2': #  모델링 하는부분
            app.modeling('train.csv', 'test.csv')


        elif menu == '0':
            break
