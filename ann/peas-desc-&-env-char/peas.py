class RobotVacuumAgent:
    def __init__(self):
        self.dirt_sensor = False
        self.obstacle_sensor = False
        self.battery_level = 100
        self.location = (0, 0)
        self.cleaning_completed = False
        self.is_cleaning = False
        self.direction = "stationary"
        self.environment = {
            "floor": [["clean", "dirty"], ["clean", "clean"]],
            "obstacles": [(1, 0)]
        }

    def detect_dirt(self):
        x, y = self.location
        if self.environment["floor"][x][y] == "dirty":
            self.dirt_sensor = True
        else:
            self.dirt_sensor = False

    def detect_obstacle(self):
        if self.location in self.environment["obstacles"]:
            self.obstacle_sensor = True
        else:
            self.obstacle_sensor = False

    def check_battery(self):
        return self.battery_level

    def move(self, direction):
        x, y = self.location
        if direction == "up" and x > 0:
            self.location = (x - 1, y)
        elif direction == "down" and x < len(self.environment["floor"]) - 1:
            self.location = (x + 1, y)
        elif direction == "left" and y > 0:
            self.location = (x, y - 1)
        elif direction == "right" and y < len(self.environment["floor"][0]) - 1:
            self.location = (x, y + 1)
        else:
            print("invalid move or boundary reached.")
        self.detect_obstacle()

    def clean(self):
        x, y = self.location
        if self.dirt_sensor:
            self.environment["floor"][x][y] = "clean"
            self.is_cleaning = True
            print(f"cleaning position {self.location}")
        else:
            self.is_cleaning = False
            print(f"no dirt at position {self.location}")

    def performance_measure(self):
        clean_tiles = sum(row.count("clean") for row in self.environment["floor"])
        total_tiles = len(self.environment["floor"]) * len(self.environment["floor"][0])
        return f"performance: {clean_tiles}/{total_tiles} tiles clean"

    def run(self):
        while not self.cleaning_completed:
            self.detect_dirt()
            self.clean()

            if self.check_battery() <= 20:
                print("low battery. returning to charging station.")
                break

            if self.environment["floor"] == [["clean", "clean"], ["clean", "clean"]]:
                print("all clean!")
                self.cleaning_completed = True
                break

            if not self.obstacle_sensor:
                self.move("right")
            else:
                print("obstacle detected, changing direction.")
                self.move("down")

            self.battery_level -= 10

        print(self.performance_measure())

# create an agent instance and run
robot_vacuum = RobotVacuumAgent()
robot_vacuum.run()
