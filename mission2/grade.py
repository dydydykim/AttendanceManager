from abc import ABC, abstractmethod

class Grade(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def is_removable(self):
        pass


class NormalGrade(Grade):
    @property
    def name(self):
        return "NORMAL"

    def is_removable(self):
        return True


class SilverGrade(Grade):
    @property
    def name(self):
        return "SILVER"

    def is_removable(self):
        return False


class GoldGrade(Grade):
    @property
    def name(self):
        return "GOLD"

    def is_removable(self):
        return False


GOLD_SCORE_THRESHOLD = 50
SILVER_SCORE_THRESHOLD = 30

#factory function to decide grade
def determine_grade_from_points(points: int) -> Grade:
    if points >= GOLD_SCORE_THRESHOLD:
        return GoldGrade()
    elif points >= SILVER_SCORE_THRESHOLD:
        return SilverGrade()
    else:
        return NormalGrade()