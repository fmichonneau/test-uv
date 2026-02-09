import duckdb
import matplotlib.pyplot as plt

# Create an in-memory DuckDB database and populate it
con = duckdb.connect()

con.execute("""
    CREATE TABLE sales (
        month VARCHAR,
        revenue DOUBLE
    )
""")

con.execute("""
    INSERT INTO sales VALUES
        ('Jan', 12000),
        ('Feb', 15000),
        ('Mar', 13500),
        ('Apr', 17000),
        ('May', 19500),
        ('Jun', 21000)
""")

# Query the data
df = con.execute("SELECT * FROM sales").fetchdf()

# Plot
fig, ax = plt.subplots()
ax.bar(df["month"], df["revenue"], color="steelblue")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue ($)")
ax.set_title("Monthly Revenue")
fig.tight_layout()
plt.show()
