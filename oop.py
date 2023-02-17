from prettytable import PrettyTable
table=PrettyTable()
print(table)
table.add_column("Pokemnon name",["pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align="l"
print(table)