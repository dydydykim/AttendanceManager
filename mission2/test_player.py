import pytest
from player import *

@pytest.fixture
def player():
    return Player("TestUser")

def test_player_initialization(player):
    assert player.name == "TestUser"
    assert player.points == 0
    assert isinstance(player.grade, NormalGrade)
    assert player.attendance_history == {}


@pytest.mark.parametrize("day, expected_points", [
    ("monday", WEEKDAY_POINT),
    ("saturday", WEEKEND_POINT),
    ("wednesday", WEDNESDAY_POINT)
])
def test_record_attendance_points(player, day, expected_points):
    player.record_attendance(day)
    assert player.points == expected_points


def test_record_attendance_history(player):
    player.record_attendance("monday")
    player.record_attendance("monday")
    player.record_attendance("wednesday")

    assert player.attendance_history["monday"] == 2
    assert player.attendance_history["wednesday"] == 1
    assert player.points == (WEEKDAY_POINT * 2) + WEDNESDAY_POINT


def test_calculate_bonus_no_bonus(player):
    #9번만 출석해서 보너스 없음
    for _ in range(BONUS_COUNT - 1):
        player.record_attendance("wednesday")
        player.record_attendance("saturday")

    initial_points = player.points
    player.calculate_bonus()
    assert player.points == initial_points


def test_calculate_bonus_for_wednesday(player):
    #수요일 보너스
    for _ in range(BONUS_COUNT):
        player.record_attendance("wednesday")

    initial_points = player.points
    player.calculate_bonus()
    assert player.points == initial_points + BONUS_POINT


def test_calculate_bonus_for_weekend(player):
    # 토요일 5번, 일요일 5번 출석
    for _ in range(5):
        player.record_attendance("saturday")
        player.record_attendance("sunday")

    initial_points = player.points
    player.calculate_bonus()
    assert player.points == initial_points + BONUS_POINT


def test_calculate_bonus_for_both(player):
    #수요일과 주말 보너스가 모두 지급되는지 테스트
    for _ in range(10):
        player.record_attendance("wednesday")
        player.record_attendance("saturday")

    initial_points = player.points
    player.calculate_bonus()
    assert player.points == initial_points + (BONUS_POINT * 2)


@pytest.mark.parametrize("points, expected_grade_class", [
    (29, NormalGrade),
    (49, SilverGrade),
    (50, GoldGrade),
    (100, GoldGrade)
])
def test_update_grade(player, points, expected_grade_class):
    player.points = points
    player.update_grade()
    assert isinstance(player.grade, expected_grade_class)


def test_is_removable_true(player):
    player.record_attendance("monday")  # points = 1 -> NormalGrade
    player.update_grade()
    assert player.is_removable() is True


def test_str_representation(player):
    player.points = 55
    player.update_grade()  # GoldGrade

    expected_str = "NAME : TestUser, POINT : 55, GRADE : GOLD"
    assert player.get_info() == expected_str