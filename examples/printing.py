"""Printing examples."""

from chroma import Level, pprint

# Just import the `pprint` function and use it as a substitute for the standard `print`.

# A trivial example.
pprint("A string.")
pprint(42)
pprint()

# Several objects are automatically pretty printed if `highlight` is True.
pprint("This is a sentences with an ellipsis...", highlight=True)
pprint("This is the path /etc/fstab.", highlight=True)
pprint("This is the URL https://www.google.com/.", highlight=True)
pprint("This is the IPv4 1.2.3.4.", highlight=True)
pprint("This is the IPv6 1:2:3:4:5:6:7:8.", highlight=True)
pprint("This is the UUID 550e8400-e29b-41d4-a716-446655440000.", highlight=True)
pprint()

# Basic data types are also pretty printed.
pprint("This is None.", highlight=True)
pprint("This is the boolean True.", highlight=True)
pprint("This is the integer 42.", highlight=True)
pprint("This is the float 42.0.", highlight=True)
pprint("This is the quoted string 'abc'.", highlight=True)
pprint()

# Collections too!
pprint(f"This is the list {[1, 2, 3]}.", highlight=True)
pprint(f"This is the set {{1, 2, 3}}.", highlight=True)
pprint(f"This is the dictionary {{'a':1,'b':2,'c':3}}.", highlight=True)
pprint()

# The `level` parameter specifies the message severity.
pprint("This is a debugging message.", level=Level.DEBUG)
pprint("This is an informational message.")
pprint("This is also an informational message.", level=Level.INFO)
pprint("This is a notice message.", level=Level.NOTICE)
pprint("This is a success message.", level=Level.SUCCESS)
pprint("This is a warning message.", level=Level.WARNING)
pprint("This is an error message.", level=Level.ERROR)
pprint("This is a critical message.", level=Level.CRITICAL)
pprint("This is an alert message.", level=Level.ALERT)
pprint("This is an emergency message.", level=Level.EMERGENCY)
