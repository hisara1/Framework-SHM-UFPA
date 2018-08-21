from components.missing_data_simulator import MissingDataSimulator
from components.missing_data_amputator import MissingDataAmputator

original_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

simulator = MissingDataSimulator(original_data, 50)

new_dataset = simulator.simulate_missing_data()

print(MissingDataAmputator(new_dataset).amputate_data())
