"""Table examples."""

from chroma import KeyValueTable, Level, Table, pprint

# The `Table` class can be used to pretty print tables.

# A simple table with three columns.
table = Table("one", "two", "three")
table.add("a", "b", "c")
table.add(1, 2, 3)
table.add(1.1, 2.2, 3.3)
table.add("a", 2, 3.3)
pprint(table)

# A simple table with a title.
table = Table("one", "two", "three", title="some title")
table.add("a", "b", "c")
table.add(1, 2, 3)
table.add(1.1, 2.2, 3.3)
table.add("a", 2, 3.3)
pprint(table)

# A table but with some highlighting.
table = Table("x", "y", highlight=True)
table.add("a", 1.0)
table.add("b", "1.2.3.4")
table.add("c", "/bin/ls")
pprint(table)

# A table with some emphasized rows.
table = Table("one", "two", "three")
table.add("a", "b", "c")
table.add(1, 2, 3, level=Level.EMPHASIS)
table.add(1.1, 2.2, 3.3, level=Level.SUCCESS)
table.add("a", 2, 3.3, level=Level.ERROR)
pprint(table)

# Key-value pairs are very common and can be printed with the special table
# class `KeyValueTable`.
table = KeyValueTable()
table.add("foo", 0.1)
table.add("bar", 0.2)
table.add("baz", 0.3)
pprint(table, highlight=True)
