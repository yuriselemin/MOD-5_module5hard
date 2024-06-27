import hashlib
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode



class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def add_user(self, user):
        self.users.append(user)


    def login(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password_hash == hashlib.sha256(password.encode()).hexdigest():
                self.current_user = user
                print("Пользователь {} авторизован".format(user.nickname))
                return True
        return False


    def register(self, nickname, password, age):
        if self.current_user is not None and self.current_user.nickname == nickname:
            print("Пользователь {} уже существует".format(nickname))
        else:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            new_user = User(nickname, password_hash, age)
            self.users.append(new_user)
            self.current_user = new_user
            print("Регистрация прошла успешно")


    def log_out(self):
        self.current_user = None


    def add(self, *videos):
        for video in videos:
            if video.title not in [vid.title for vid in self.videos]:
                self.videos.append(video)


    def get_videos(self, search_word):
        result = [video.title for video in self.videos if search_word.lower() in video.title.lower()]
        return result


    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        age_restricted_video = False
        if self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return


        for video in self.videos:
            if video.title == title:
                break
        else:
            print("Видео не найдено")
            return

        for second in range(video.duration):
            time.sleep(1)
            print(f"{second + 1}: воспроизведение видео...")
        print("Конец видео")


if __name__ == '__main__':
   ur = UrTube()

   v1 = Video('Лучший язык программирования 2024 года', 200)
   v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

   ur.add(v1, v2)

   print(ur.get_videos('лучший'))
   print(ur.get_videos('ПРОГ'))

   ur.watch_video('Для чего девушкам парень программист?')
   ur.register('vasya_pupkin', 'lolkekcheburek', 13)
   ur.watch_video('Для чего девушкам парень программист?')
   ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
   ur.watch_video('Для чего девушкам парень программист?')
   ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
   print(ur.current_user)

   ur.watch_video('Лучший язык программирования 2024 года!')



