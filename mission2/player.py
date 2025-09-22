from grade import *

GOLD_SCORE = 50
SILVER_SCORE = 30

WEEKDAY_POINT = 1
WEEKEND_POINT = 2
WEDNESDAY_POINT = 3

BONUS_COUNT = 10
BONUS_POINT = 10

WEEK_DAYS = {"monday", "tuesday", "wednesday", "thursday", "friday"}
WEEKEND_DAYS = {"saturday", "sunday"}

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.grade = NormalGrade()
        self.attendance_history = {}

    def record_attendance(self, day):
        self.attendance_history[day] = self.attendance_history.get(day, 0) + 1

        if day == "wednesday":
            self.points += WEDNESDAY_POINT
        elif day in WEEK_DAYS:
            self.points += WEEKDAY_POINT
        elif day in WEEKEND_DAYS:
            self.points += WEEKEND_POINT

    def calculate_bonus(self):
        if self.attendance_history.get("wednesday", 0 ) >= BONUS_COUNT:
            self.points += BONUS_POINT

        weekend_total = self.attendance_history.get("saturday", 0)
        weekend_total += self.attendance_history.get("sunday", 0)

        if weekend_total >= BONUS_COUNT:
            self.points += BONUS_POINT

    def update_grade(self):
        self.grade = determine_grade_from_points(self.points)

    def is_removable(self):
        is_attended_special_Day = self.attendance_history.get("wednesday", 0) > 0 or \
                                  self.attendance_history.get("saturday", 0) > 0 or \
                                  self.attendance_history.get("sunday", 0) > 0
        return self.grade.is_removable() and not is_attended_special_Day


    def get_info(self):
        return f"NAME : {self.name}, POINT : {self.points}, GRADE : {self.grade.name}"
