from player import Player

players = {}
MAX_LINES_TO_READ = 500
FILE_PATH = "attendance_weekday_500.txt"


def process_attendance():
    try:
        load_data()
        process_scores()
        print_result()

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")


def load_data():
    with open("attendance_weekday_500.txt", encoding='utf-8') as f:
        for _ in range(MAX_LINES_TO_READ):
            line = f.readline()
            if not line:
                break
            parts = line.strip().split()
            if len(parts) == 2:
                record_attendance(parts[0], parts[1])


def record_attendance(name, attendance_day):
    if name not in players:
        players[name] = Player(name)

    player = players[name]
    player.record_attendance(attendance_day)


def process_scores():
    for player in players.values():
        player.calculate_bonus()
        player.update_grade()


def print_result():
    for player in players.values():
        print(player.get_info())

    print("\nRemoved player")
    print("==============")

    for player in players.values():
        if player.is_removable():
            print(player.name)


if __name__ == "__main__":
    process_attendance()