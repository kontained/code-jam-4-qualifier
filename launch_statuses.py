from enum import Enum, unique


@unique
class LaunchStatus(Enum):
    LaunchNotInitiated = 1
    Status1 = 2
    Status2 = 3
    Status3 = 4
    Launched = 5
