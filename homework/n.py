import sqlite3, pandas as pd

conn = sqlite3.connect(":memory:")
with open("tests/create_tables.sql") as f:
    conn.cursor().executescript(f.read())

result = pd.read_sql_query("SELECT K0, avg(c12) FROM tbl1 WHERE c13 > 400 GROUP BY K0 ORDER BY K0", conn).to_dict()
result['avg(c12)'] = {k: round(v, 2) for k, v in result['avg(c12)'].items()}
print(result)