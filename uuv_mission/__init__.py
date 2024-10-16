from dynamic import Mission
import os

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(dir, 'data', 'mission.csv')

mission = Mission.from_csv(csv_path)
print(mission)