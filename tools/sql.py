import sqlite3
from pydantic.v1 import BaseModel
from typing import List
from langchain.tools import Tool

conn = sqlite3.connect('db.sqlite')


def list_tables():
    c = conn.cursor()
    c.execute("Select name from sqlite_master where type='table'")
    rows = c.fetchall()
    return "\n".join(row[0] for row in rows if row[0] is not None)


def describe_table(table_names):
    c = conn.cursor()
    tables = ', '.join("'" + table + "'" for table in table_names)
    rows = c.execute(f"Select name from sqlite_master where type='table' and name in ({tables});")
    return '\n'.join(row[0] for row in rows if row[0] is not None)


def run_sqlite_query(query):
    c = conn.cursor()
    try:
        c.execute(query)
        return c.fetchall()
    except sqlite3.OperationalError as e:
        return f"the following error occurred: {e}"


class RunQueryArgsSchema(BaseModel):
    query: str


class DescribeTableArgsSchema(BaseModel):
    table_names: str


run_query_tool = Tool.from_function(
    name='run_sqlite_query',
    description="run sql query",
    func=run_sqlite_query,
    args_schema=RunQueryArgsSchema
)

describe_table_tool = Tool.from_function(
    name='describe_table',
    description="describe tables",
    func=describe_table,
    args_schema=DescribeTableArgsSchema
)
