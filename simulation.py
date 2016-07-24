import printersim_class
import pythonds
import random
import time

def simulation(num_seconds, pages_per_minute):
    lab_printer = printersim_class.Printer(pages_per_minute)
    print_queue = pythonds.Queue()
    waiting_times = []

    for current_second in range(num_seconds):

        if new_print_task():
            task = printersim_class.Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("average wait time %6.2f seconds %3d tasks remaining"
        %(average_wait, print_queue.size()))
    time.sleep(1)
        
def new_print_task():
    num = random.randrange(1, 361)
    if num == 360:
        return True
    else:
        return False

for i in range(10):
    simulation(3600, 5)
