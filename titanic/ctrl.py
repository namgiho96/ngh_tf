from titanic.entity import Entity
from titanic.titanic_service import TitanicService


class Ctrl:
    def __init__(self):
        self.entity = Entity()
        self.titanicService = TitanicService()

    def modeling(self, train, test):  # 모델링 하는 함수
        service = self.titanicService
        this = self.preprocess(train, test)
        this.label = service.creat_lable(this)
        this.train = service.crate_train(this)
        return this

    def preprocess(self, train, test) -> object:  # 전처리 하는 함수 #  데이터 모델릴 하는 함수
        titanicService = self.titanicService
        this = self.entity
        this.train = titanicService.new_model(train)
        this.test = titanicService.new_model(test)
        this.id = this.test['PassengerId']
        this = titanicService.drop_feature(this, 'Cabin')
        this = titanicService.drop_feature(this, 'Ticket')
        this = titanicService.embarked_nominal(this)
        this = titanicService.title_nominal(this)
        this = titanicService.drop_feature(this, 'Name')
        this = titanicService.drop_feature(this, 'PassengerId')
        this = titanicService.age_ordinal(this)
        this = titanicService.sex_nominal(this)
        this = titanicService.fareBand_nominal(this)
        this = titanicService.drop_feature(this, 'Fare')
        print(f'train 전처리 마감 후 컬럼 : {this.train.columns}')
        print(f'test 전처리 마감 후 컬럼 : {this.train.columns}')
        print(f'train 널의 수량  : {this.train.isnull().sum()}')
        print(f'test 널의 수량  : {this.test.isnull().sum()}')

        return this

    def learning(self, train, test):  # 여기서 러닝
        service = self.titanicService
        this = self.modeling(train, test)
        print(f'KNN 활용한 검증 정확도 {None}')
        print(f'결정트리 활용한 검증 정확도 {None}')
        print(f'랜덤포레스트 활용한 검증 정확도 {None}')
        print(f'나이브배이즈 활용한 검증 정확도 {None}')
        print(f'SVM 활용한 검증 정확도 {None}')

