def assign_tables(groups: dict[str, list[str]], tables_num: int):
    max_len = 0
    for members in groups.values():
        for name in members:
            if len(name) > max_len:
                max_len = len(name)

    fib = [0] * (max_len + 2)
    fib[1] = 1
    for i in range(2, max_len + 2):
        fib[i] = fib[i - 1] + fib[i - 2]

    def hash_name(name):
        h = 0
        for i, ch in enumerate(name, start=1):
            h += ord(ch) * fib[i]
        return h

    tables = {}
    collisions = []
    last_team = {}

    for team, members in groups.items():
        total = 0
        for member in members:
            total += hash_name(member)

        table = (total * len(members)) % tables_num
        tables[team] = table

        if table in last_team:
            collisions.append((team, table, last_team[table]))

        last_team[table] = team

    return tables, collisions