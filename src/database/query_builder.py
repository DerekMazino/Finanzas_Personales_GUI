class QueryBuilder:
    def __init__(self, table):
        self.table = table
        self._query = ""
        self._params = []

    def select(self, columns="*"):
        self._query = f"SELECT {columns} FROM {self.table}"
        return self

    def insert(self, data: dict):
        keys = ", ".join(data.keys())
        placeholders = ", ".join(["?"] * len(data))
        self._query = f"INSERT INTO {self.table} ({keys}) VALUES ({placeholders})"
        self._params = list(data.values())
        return self

    def where(self, column, value, operator="="):
        if "WHERE" not in self._query:
            self._query += f" WHERE {column} {operator} ?"
        else:
            self._query += f" AND {column} {operator} ?"
        self._params.append(value)
        return self

    def build(self):
        return self._query, tuple(self._params)
