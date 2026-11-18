# class Person():
#     ism = 'Saipnazar'
#     familiya = 'Saipnazarov'
#     yosh = '15'
#     manzil = 'Xiva Shahar'
#     kasb = 'Oquvchi'
# print(Person.ism)


# class Person:
#     def init(self, ism, familiya, yosh, ish_joyi, manzil):
#         self.ism = ism
#         self.familiya = familiya
#         self.yosh = yosh
#         self.ish_joyi = ish_joyi
#         self.manzil = manzil

#     def str(self):
#         return (
#             f'ismi--> {self.ism}\n'
#             f'familiya--> {self.familiya}\n'
#             f'yosh--> {self.yosh}\n'
#             f'ish_joyi--> {self.ish_joyi}\n'
#             f'manzil--> {self.manzil}'
#         )


# p1 = Person('Mustafo', 'Polvanazirov', 17, 'ishsiz', 'Xiva Shahar')
# p2 = Person('Saipnazar', 'Saipnazarov', 15, 'ishsiz', 'Xiva Shahar')
# p3 = Person('Azizbek', 'Atobayev', 13, 'ishsiz', 'Xiva Shahar')

# print(p1)
# print(p2)
# print(p3)

class Talaba:
    def __init__(self, ism, familiya, yosh, universitet, kurs):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        self.universitet = universitet
        self.kurs = kurs

    def __str__(self):
        return (
            f'ism--> {self.ism}\n'
            f'familiya--> {self.familiya}\n'
            f'yosh--> {self.yosh}\n'
            f'universitet--> {self.universitet}\n'
            f'kurs--> {self.kurs}'
        )


p1 = Talaba('Ali', 'Valiyev', 20, 'TATU', 3)
print(p1)
