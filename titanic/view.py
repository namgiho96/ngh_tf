from titanic.titanic_service import TitanicService
from titanic.entity import Entity
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns
rc

class View:
    def __init__(self, fname):
        service = TitanicService()
        entity = Entity()
        entity.fname = fname
        entity.context = './data/'
        self._entity = service.new_model(entity)


    def plot_survived_dead(self):
        this = self._entity
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        this['Survived'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0. 사망자 vs 1.생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0. 사망자 vs 1.생존자')
        sns.countplot('Survived', data=this, ax=ax[1])
        plt.show()

    def plot_sex(self):
        this = self._entity
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        this['Survived'][this['Sex'] == 'male'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        this['Survived'][this['Sex'] == 'female'].value_counts().plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1], shadow=True)
        ax[0].set_title('남성의 생존비율 [0. 사망자 vs 1.생존자]')
        ax[1].set_title('여성의 생존비율 [0. 사망자 vs 1.생존자]')
        plt.show()







