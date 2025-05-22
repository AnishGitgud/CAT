import random
import time

class Table:
    def __init__(self, size: int):
        self.table = []
        self.rows = size
        self.columns = size
        self.row_head = []
        self.col_head = []
        self.solved_table = []

    def set_heads(self):
        """Set the row and column heads with random numbers."""
        all_numbers = random.sample(range(10,100), self.rows + self.columns)
        self.row_head = all_numbers[:self.rows]
        self.col_head = all_numbers[self.rows:]

    def set_table(self):
        """Initialize the table with 'Null' for empty cells."""
        try:
            r1 = []
            r1.append('Heads')
            for rH in self.row_head:
                r1.append(str(rH))
            r1.append('Total')
            self.table.append(r1)   # row head set

            rx = []
            for h in self.col_head:
                rx.append(str(h))
                for i in range(self.rows):
                    rx.append('Null')
                rx.append('Null')
                self.table.append(rx)
                rx = []

            self.table.append(['Total'] + ['Null'] * (self.rows + 1))
        except Exception as e:
            print(f"Error: {e}\nSet Heads first")

    def calculate_values(self):
        """Calculate values for the table."""
        try:
            rx = []
            for i in range(1, len(self.table) - 1):
                for j in range(1, len(self.table[i]) - 1):
                    rx.append(str(self.col_head[i-1] + self.row_head[j-1]))
                self.solved_table.append(rx)
                rx = []
        except Exception as e:
            print(f"Error: {e}\nSet Heads first")

    def reset_table(self):
        """Reset the table to generate new numbers."""
        self.table = []
        self.solved_table = []
        self.set_heads()
        self.set_table()
        self.calculate_values()

class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = 0

    def start(self):
        """start the timer."""
        self.start_time = time.time()
        self.end_time = None
        self.elapsed_time = 0

    def stop(self):
        """stop the timer and calculate elapsed time."""
        if self.start_time:
            self.end_time = time.time()
            self.elapsed_time = self.end_time - self.start_time
            return self.elapsed_time
        return 0
    
    def get_elapsed_time(self):
        """Get current elapsed time for live display."""
        if self.start_time and not self.end_time:
            return time.time() - self.start_time
        return self.elapsed_time
    
    def format_time(self):
        """Format time into MM:SS format."""
        seconds = self.get_elapsed_time()
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes:02d}:{seconds:02d}"
    
    def is_running(self):
        """Check if the timer is running."""
        return self.start_time is not None and self.end_time is None


### Below is just for testing
def main():
    table = Table(10)
    table.set_heads()
    print(f"Row heads: {table.row_head}\nColumn heads: {table.col_head}")
    table.set_table()
    print("\nTable: ")
    for i in range(len(table.table)):
        print(f"{table.table[i]}")
    table.calculate_values()
    print("\nSolved table: ")
    for j in range(len(table.solved_table)):
        print(f"{table.solved_table[j]}")

if __name__=="__main__":
    main()