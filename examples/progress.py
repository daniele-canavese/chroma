"""Progress bar examples."""

from random import random
from time import sleep

from chroma import ProgressBar, Table, pprint

# The `ProgressBar` class supports dynamic progress bars.

# A simple progress bar.
for i in ProgressBar(range(1000)):
    sleep(0.001)

# A progress bar with a description.
for i in ProgressBar(range(1000), description="doing stuff..."):
    sleep(0.001)

# Printing something while a progress bar is running.
for i in ProgressBar(range(10)):
    pprint("iteration", i, highlight=True)
    sleep(0.25)

# A progress bar with multiple tasks.
with ProgressBar(description="multi tasking") as progress:
    task1 = progress.add_task(description="task 1", total=10)
    for i in range(10):
        progress.update_task(task1)
        sleep(0.1)
    progress.remove_task(task1)
    task2 = progress.add_task(description="task 2", total=10)
    for i in range(10):
        progress.update_task(task2)
        sleep(0.1)
    progress.remove_task(task2)

# Updating a table while a progress bar is running using the `table` parameter of the `ProgressBar`
# class.
table = Table("what", "number", highlight=True)
for i in ProgressBar(range(1000), table=table):
    if not i % 42:
        table.add("random", random())  # nosec B311
    sleep(0.001)
