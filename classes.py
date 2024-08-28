class MyName:
    name:str = 'Alex' # public
    _bithday:int=1990 # protected доступен в классе и его потомках
    __last_name:str = 'Ivanov' # private доступен только в классе
    parent_id:int

    def __new__(cls, *args,**kwargs):
        print('new')
        instn= super().__new__(cls)
        # print(f'{instn.parent_id}') ошибка так как инстенц пустой и свойство ему не добавлено
        return instn


    def __init__(self,parent_id:int,pet_name:str):
        print('init')
        self.parent_id=parent_id
        self.pet_name = pet_name
        
    def _get_bithday(self,*args,**kwargs): # protected , method
        self.name = 'Artiom'

    @staticmethod
    def get_age(year):
        pass

    @classmethod
    def do_something(cls,*args,**kwargs):
        cls.pet_name = 'Name'
        cls.parent_id = args[0]


# MyName.get_age(1990)
# MyName.do_something(1)
my_name = MyName(2,'Tobu')



my_dictionary = {k:v for k,v in enumerate(range(10))}
print(my_dictionary)
