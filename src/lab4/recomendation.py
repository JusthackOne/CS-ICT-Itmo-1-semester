import os


class Recomendation:
    def __init__(self):
        self.history_file = os.path.join(os.path.dirname(__file__), 'history.txt')
        self.films_file = os.path.join(os.path.dirname(__file__), 'films.txt')

    # Преобразование истории пользователся
    def get_user_history(self):
        history_input = input()
        user_history = set(history_input.split(','))
        print(user_history)
        return user_history

    # Получение всех списков фильмов, которые подходят под рекомендации
    def get_recomendation_history_users(self, history):
        with open(self.history_file, 'r') as file:
            histories = [set(history.strip().split(',')) for history in file.readlines() if history != '\n']
            file.close()

        recomendationHistories = list()
        history_length = len(history)
        for user in histories:
            count = 0
            recommendation_list = list()
            for film in user:
                if film in history:
                    count +=1
                else:
                    recommendation_list.append(film)

            if len(recommendation_list) == 0:
                continue
            recommendation_list = sorted(recommendation_list)
            # Если кол-во одинаковых просмотренных фильмов больше половины
            # (не строго), то добавляем это в список рекомендаций
            # в конец всякого коректного списка мы добавляем вес рекомендаций
            if history_length%2==0:
                if count >= (history_length//2):
                    recommendation_list.append(count/history_length)
                    recomendationHistories.append(recommendation_list)
            else:
                if count >= (history_length//2)+1:
                    recommendation_list.append(count / history_length)
                    recomendationHistories.append(recommendation_list)
        print(recomendationHistories)
        return recomendationHistories
    # Получение ID рекомендованных фильмов
    def get_recomendation_list(self, recomendationHistories):
        recomendationList = {}
        for history in recomendationHistories:
            for film in range(len(history) - 1):
                key = recomendationList.get(history[film])
                if key is not None:
                    recomendationList[history[film]] *= history[-1]
                else:
                    recomendationList[history[film]] = history[-1]
        print(recomendationList)
        return recomendationList

    # Получение ID фильма, который входит в список
    # рекомендации и встречаеться чаще всего
    def get_recomendation_film_id(self, recomendationList):
        with open(self.history_file, 'r') as file:
            histories = [history.strip().split(',') for history in file.readlines() if history != '\n']
            file.close()

        films_counts = {}
        # Считаем, сколько просмотров в общем поиске
        for recomendationFilm in recomendationList:

            result = 0
            for history in histories:
                result += history.count(recomendationFilm)
            # Добавляем результат алгоритма - кол-во результатов всего умноженное на вес фильма
            films_counts[recomendationFilm] = result*recomendationList[recomendationFilm]
        print(films_counts)
        recomendationFilmId = max(films_counts, key=films_counts.get)
        print(recomendationFilmId)
        return recomendationFilmId

    # Получение названия фильма по ID
    def get_recomendation_film_name(self, recomendationFilmId):
        with open(self.films_file, 'r', encoding="utf-8") as file:
            films = [film.strip().split(',') for film in file.readlines() if film != '\n']

            file.close()

        return films[int(recomendationFilmId)-1][1]

if __name__ == "__main__":
    recomendation = Recomendation()
    history = recomendation.get_user_history()
    recomendationHistories = recomendation.get_recomendation_history_users(history)
    recomendationList = recomendation.get_recomendation_list(recomendationHistories)
    recomendationFilmId = recomendation.get_recomendation_film_id(recomendationList)
    recomendationFilmName = recomendation.get_recomendation_film_name(recomendationFilmId)

    print(recomendationFilmName)