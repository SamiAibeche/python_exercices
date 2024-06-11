import threading
from natsort import natsorted
import os


class ReadFileThread(threading.Thread):
    def __init__(self, filename, index, results, lock):
        super().__init__()
        self.filename = filename
        self.index = index
        self.results = results
        self.lock = lock

    def run(self):
        with open(self.filename, 'r') as file:
            content = file.read()
        with self.lock:
            self.results[self.index] = content


def gather_sonnets(input_folder, output_file):
    # List all files in the input folder
    files = natsorted([os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.txt')])

    # Dictionary to store results with file index as key
    results = {}
    lock = threading.Lock()

    # Create and start threads
    threads = []
    for index, filename in enumerate(files):
        thread = ReadFileThread(filename, index, results, lock)
        thread.start()
        threads.append(thread)

    # Join threads
    for thread in threads:
        thread.join()

    # Write results to the output file in order
    with open(output_file, 'w') as output:
        for index in sorted(results.keys()):
            output.write(results[index])
            output.write("\n")  # Ensure each file's content is separated by a newline


# Define input folder and output file
input_folder = 'data'
output_file = 'data_all.txt'

# Gather all sonnets into one file
gather_sonnets(input_folder, output_file)