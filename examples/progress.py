"""Progress bar examples."""

from random import random
from time import sleep

from chroma import ProgressBar, Table, pprint

# The `ProgressBar` class supports dynamic progress bars.

# A simple progress bar.
for i in ProgressBar(range(1000)):
    # nosemgrep: python.lang.best-practice.sleep.arbitrary-sleep
    sleep(0.001)  # nosemgrep: python.lang.best-practice.sleep.arbitrary-sleep

# A progress bar with a description.
for i in ProgressBar(range(1000), description="doing stuff..."):
    # nosemgrep: python.lang.best-practice.sleep.arbitrary-sleep
    sleep(0.001)  # nosemgrep: python.lang.best-practice.sleep.arbitrary-sleep

# Printing something while a progress bar is running.
for i in ProgressBar(range(10)):
    pprint("iteration", i, highlight=True)
    # nosemgrep: python.lang.best-practice.sleep.arbitrary-sleep
    sleep(0.25)  # nosemgrep: python.lang.best-practice.sleep.arbitrary-sleep

# Updating a table while a progress bar is running using the `table` parameter of the `ProgressBar` class.
table = Table("what", "number", highlight=True)
for i in ProgressBar(range(1000), table=table):
    if i % 42 == 0:
        table.add("random", random())
    # nosemgrep: python.lang.best-practice.sleep.arbitrary-sleep
    sleep(0.001)  # nosemgrep: python.lang.best-practice.sleep.arbitrary-sleep
