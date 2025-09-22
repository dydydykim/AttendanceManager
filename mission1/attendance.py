name_to_id = {}
user_count = 0

DAY_TO_INDEX = {
    "monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6
}
WEEK_DAYS = {"monday", "tuesday", "wednesday", "thursday", "friday"}
WEEKEND_DAYS = {"saturday", "sunday"}

MAX_USERS = 100
MAX_DAY_NUM = 100
MAX_LINES_TO_READ = 500

NORMAL_GRADE = 0
GOLD_GRADE = 1
SILVER_GRADE = 2

GOLD_SCORE = 50
SILVER_SCORE = 30

WEEKDAY_POINT = 1
WEEKEND_POINT = 2
WEDNESDAY_POINT = 3

BONUS_COUNT = 10
BONUS_POINT = 10

# attend_history[사용자ID][요일]
attendance_history = [[0] * MAX_DAY_NUM for _ in range(MAX_USERS)]
points = [0] * MAX_USERS
grade = [0] * MAX_USERS
names = [''] * MAX_USERS
wednesday_count = [0] * MAX_USERS
weekend_count = [0] * MAX_USERS


def process_attendance():
    try:
        load_data()
        calculate_bonus()
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
    if name not in name_to_id:
        assign_id_to_user(name)

    id = name_to_id[name]

    index = get_day_index(attendance_day)
    point = get_point_for_day(attendance_day)

    attendance_history[id][index] += 1
    points[id] += point

    update_special_day_count(attendance_day, id)


def update_special_day_count(attendance_day, id):
    if attendance_day == "wednesday":
        wednesday_count[id] += 1
    if attendance_day in WEEKEND_DAYS:
        weekend_count[id] += 1


def get_point_for_day(attend_day) -> int:
    point = 0
    if attend_day == "wednesday":
        point += WEDNESDAY_POINT
    elif attend_day in WEEK_DAYS:
        point += WEEKDAY_POINT
    elif attend_day in WEEKEND_DAYS:
        point += WEEKEND_POINT
    return point


def get_day_index(attend_day) -> int:
    return DAY_TO_INDEX[attend_day]


def assign_id_to_user(name):
    global user_count
    user_count += 1
    name_to_id[name] = user_count
    names[user_count] = name


def calculate_bonus():
    for id in range(1, user_count + 1):
        if attendance_history[id][DAY_TO_INDEX["wednesday"]] >= BONUS_COUNT:
            points[id] += BONUS_POINT
        if attendance_history[id][DAY_TO_INDEX['saturday']] + attendance_history[id][DAY_TO_INDEX['sunday']] >= BONUS_COUNT:
            points[id] += BONUS_POINT

        if points[id] >= GOLD_SCORE:
            grade[id] = GOLD_GRADE
        elif points[id] >= SILVER_SCORE:
            grade[id] = SILVER_GRADE
        else:
            grade[id] = NORMAL_GRADE


def print_result():
    print_grade()
    print_removed_players()


def print_removed_players():
    print("\nRemoved player")
    print("==============")
    for id in range(1, user_count + 1):
        if grade[id] == NORMAL_GRADE and wednesday_count[id] == 0 and weekend_count[id] == 0:
            print(names[id])


def print_grade():
    for id in range(1, user_count + 1):
        print(f"NAME : {names[id]}, POINT : {points[id]}, GRADE : ", end="")
        if grade[id] == GOLD_GRADE:
            print("GOLD")
        elif grade[id] == SILVER_GRADE:
            print("SILVER")
        else:
            print("NORMAL")


if __name__ == "__main__":
    process_attendance()