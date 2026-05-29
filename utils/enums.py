from enum import Enum


class GoalType(str, Enum):
    mass = "mass"

    cut = "cut"

    maintain = "maintain"