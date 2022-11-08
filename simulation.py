from termcolor import colored
import random

class AirlineOverbookingSimulation():
    """Overall class for the airline overbooking simulation project."""
    
    def __init__(self):
        """Initialize attributes and behaviors of the simulation."""
        # Initialize overall random digit table, storing it as a string.
        self.overall_table = ""
        # Set passenger number.
        self.total_passengers = 22

    def generate_RDT(self):
        """Generate a random digit table."""
        random_digit_table = []
        # Generate 22 random digits for the 22 passengers in 1 trial.
        for x in range(self.total_passengers):
            # Numbers will be from 00-99.
            # Note: will not print out double digits if the numbers are less than 10.
            rand_num = random.randint(0, 99)
            # Append to the current random digit table.
            random_digit_table.append(rand_num)
            
        return random_digit_table
    
    def run_trial(self, trial_num):
        """Run one trial of the simulation."""
        current_table = self.generate_RDT()
        show = 0
        
        for num in current_table:
            # 00-08 is no-show passengers.
            if num <= 8:
                self.overall_table += colored(f"0 {num}", 'red', attrs=['reverse', 'blink'])
            # 09-99 is passengers who showed up.
            elif num >= 9:
                if num == 9:
                    self.overall_table += colored(f"0 {num}", 'blue', attrs=['reverse', 'blink'])
                else:
                    self.overall_table += colored(f"{' '.join(str(num))}", 'blue', attrs=['reverse', 'blink'])
                    
                show += 1
                
            # Add a space between after this number in overall_table.
            self.overall_table += " "
        
        # Go to the next line of overall_table.
        self.overall_table += "\n\n" 
        
        # Record the results.   
        self._recordResult(trial_num, show)
    
    def _recordResult(self, trial_num, show):
        """Record the data of the trial to a .txt file."""
        with open('results.txt', 'a') as file:
            file.write(f"{trial_num} \t{show} \n") 