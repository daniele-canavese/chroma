"""Progress bar examples."""

from random import random
from time import sleep

from chroma import ProgressBar, Table, pprint

# The `ProgressBar` class supports dynamic progress bars.

# A simple progress bar.
for i in ProgressBar(range(1000)):
    # nosemgrep
    sleep(0.001)  # nosemgrep

# A progress bar with a description.
for i in ProgressBar(range(1000), description="doing stuff..."):
    sleep(0.001)

# Printing something while a progress bar is running.
for i in ProgressBar(range(10)):
    pprint("iteration", i, highlight=True)
    sleep(0.25)  # nosemgrep:arbitrary-sleep

# Updating a table while a progress bar is running using the `table` parameter of the `ProgressBar` class.
table = Table("what", "number", highlight=True)
for i in ProgressBar(range(1000), table=table):
    if i % 42 == 0:
        table.add("random", random())  # nosec B311
    sleep(0.001)
