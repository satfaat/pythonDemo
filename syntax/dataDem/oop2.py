

class Yak1:
    name = "Tom"
    age = 22
    def setAge(age): return age

    def getAge():
        return Yak1.age


Yak1.getAge()


class Nik:
    name = 'Fire'
    def getName(): return Nik.name


data_in_list = Yak1, Nik
print(data_in_list[1].name) 

class Data:
    yak = Yak1
    nik = Nik


print(Data.yak.age) 
