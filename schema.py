#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect('master.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        email VARCHAR(32),
        password VARCHAR(32),
        balance FLOAT
    );"""
)

cursor.execute(
    """CREATE TABLE positions(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        ticker_symbol VARCHAR,
        number_of_shares INTEGER,
        vwap FLOAT
    );"""
)

cursor.execute(
    """CREATE TABLE transactions(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        unix_time FLOAT,
        transaction_type BOOL,
        last_price FLOAT,
        trade_volume INTEGER,
        ticker_symbol VARCHAR
    );"""
)

cursor.close()
connection.close()
