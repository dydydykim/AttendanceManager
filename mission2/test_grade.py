import pytest
from grade import *

@pytest.mark.parametrize("points, expected_class, expected_name, expected_removable", [
    # Gold 등급 테스트 케이스
    (GOLD_SCORE_THRESHOLD, GoldGrade, "GOLD", False),
    (GOLD_SCORE_THRESHOLD + 1, GoldGrade, "GOLD", False),
    (100, GoldGrade, "GOLD", False),

    # Silver 등급 테스트 케이스
    (SILVER_SCORE_THRESHOLD, SilverGrade, "SILVER", False),
    (SILVER_SCORE_THRESHOLD + 1, SilverGrade, "SILVER", False),
    (GOLD_SCORE_THRESHOLD - 1, SilverGrade, "SILVER", False),

    # Normal 등급 테스트 케이스
    (SILVER_SCORE_THRESHOLD - 1, NormalGrade, "NORMAL", True),
    (0, NormalGrade, "NORMAL", True),
    (-10, NormalGrade, "NORMAL", True)
])
def test_determine_grade_and_its_methods(points, expected_class, expected_name, expected_removable):

    actual_grade = determine_grade_from_points(points)

    removable = actual_grade.is_removable()
    name = actual_grade.name

    assert isinstance(actual_grade, expected_class)
    assert name == expected_name
    assert removable == expected_removable