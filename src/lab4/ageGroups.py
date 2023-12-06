class AgeGroups:
    def __init__(self):
        self.ageGroups = []
        self.respondents = []
        self.maxAge = '123'
        self.minAge = '-1'

    def set_ageGroups(self): #Установление возрастных групп
        ages = input().split(' ')

        self.ageGroups.append([self.minAge, ages[0]])
        for age in range(len(ages)-1):
            self.ageGroups.append([ages[age], ages[age+1]])
        self.ageGroups.append([ages[-1], self.maxAge])

        self.ageGroups = list(reversed(self.ageGroups))
        print(self.ageGroups)
    def set_respondents(self): #Внесение людей в список
        data = input()
        while data != 'END':
            self.respondents.append(data.split(','))
            data = input()
        print(self.respondents)

    def sort_respondents(self): #Сортировка людей
        for ageGroup in range(len(self.ageGroups)):
            minAge = int(self.ageGroups[ageGroup][0]) + 1 #Установление минимального возраста у группы
            maxAge = int(self.ageGroups[ageGroup][1]) #Установление максимального возраста у группы

            respondents_list = self.get_respondents_group(minAge, maxAge) #Получение группы, которая подходит под данную группу
            if len(respondents_list) == 0:
                continue
            sorted_respondents_by_age_name = self.sort_respondents_by_age_name(respondents_list) # Сортировка группы по возрасту и ФИО
            self.display_respondents_group(sorted_respondents_by_age_name, minAge, maxAge) # Вывод группы в консоль


    def get_respondents_group(self, minAge, maxAge):
        respondents_list = []
        for respondent in range(len(self.respondents)):
            ageRespondent = int(self.respondents[respondent][1])
            if minAge <= ageRespondent <= maxAge: # Если возраст попадает под данную группу
                respondents_list.append(self.respondents[respondent])
        return respondents_list

    def sort_respondents_by_age_name(self, respondents_list):
        sorted_respondents = sorted(respondents_list, key=lambda age: (-int(age[1]), age[0]))
        return sorted_respondents

    def display_respondents_group(self, respondents_list, minAge, maxAge):
        text = ''

        age = f'{minAge}-{maxAge}:'
        if str(maxAge) == self.maxAge:
            age = f'{minAge}+:'
        text+=age
        for respondents in respondents_list:
            respondent = f' {respondents[0]} ({respondents[1]}),'
            text+=respondent

        print(text[:-1])

if __name__ == "__main__":
    ageGroups = AgeGroups()

    ageGroups.set_ageGroups()
    ageGroups.set_respondents()
    ageGroups.sort_respondents()
