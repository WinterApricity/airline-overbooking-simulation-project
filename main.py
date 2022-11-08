from simulation import AirlineOverbookingSimulation  

# Create the simulation.    
simulation = AirlineOverbookingSimulation()
# Run 30 trials of the simulation.
for trial in range(1, 31):
    simulation.run_trial(trial)
    
# Print a copy of the random digit table that was used to copy-paste in Google Docs.
print(simulation.overall_table)