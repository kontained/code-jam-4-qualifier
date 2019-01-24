from launch_statuses import LaunchStatus


class LaunchHelper():
    def __init__(self):
        self.launch_status = LaunchStatus.LaunchNotInitiated
        self.launch_status_text = {
            LaunchStatus.LaunchNotInitiated: 'Launch',
            LaunchStatus.Status1: '3',
            LaunchStatus.Status2: '2',
            LaunchStatus.Status3: '1',
            LaunchStatus.Launched: 'Liftoff!',
        }

    def increment_countdown(self):
        if self.launch_status is LaunchStatus.Launched:
            return

        self.launch_status = LaunchStatus(self.launch_status.value + 1)

    def get_countdown_text(self):
        return self.launch_status_text[self.launch_status]
