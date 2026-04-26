import sqlite3
import pandas as pd


# PART 1: PLANETS DATABASE


def step1_no_moons():
    conn = sqlite3.connect("planets.db")
    df = pd.read_sql("""
        SELECT * FROM planets
        WHERE number_of_moons = 0;
    """, conn)
    conn.close()
    return df


def step2_name_seven():
    conn = sqlite3.connect("planets.db")
    df = pd.read_sql("""
        SELECT name, mass
        FROM planets
        WHERE LENGTH(name) = 7;
    """, conn)
    conn.close()
    return df


def step3_mass():
    conn = sqlite3.connect("planets.db")
    df = pd.read_sql("""
        SELECT name, mass
        FROM planets
        WHERE mass <= 1.00;
    """, conn)
    conn.close()
    return df


def step4_mass_moon():
    conn = sqlite3.connect("planets.db")
    df = pd.read_sql("""
        SELECT *
        FROM planets
        WHERE number_of_moons >= 1
          AND mass < 1.00;
    """, conn)
    conn.close()
    return df


def step5_blue():
    conn = sqlite3.connect("planets.db")
    df = pd.read_sql("""
        SELECT name, color
        FROM planets
        WHERE color LIKE '%blue%';
    """, conn)
    conn.close()
    return df


# PART 3: DOGS DATABASE


def step6_hungry():
    conn = sqlite3.connect("dogs.db")
    df = pd.read_sql("""
        SELECT name, age, breed
        FROM dogs
        WHERE hungry = 1
        ORDER BY age ASC;
    """, conn)
    conn.close()
    return df


def step7_hungry_age_range():
    conn = sqlite3.connect("dogs.db")
    df = pd.read_sql("""
        SELECT name, age, hungry
        FROM dogs
        WHERE hungry = 1
          AND age BETWEEN 2 AND 7
        ORDER BY name ASC;
    """, conn)
    conn.close()
    return df


def step8_oldest_4():
    conn = sqlite3.connect("dogs.db")
    df = pd.read_sql("""
        SELECT name, age, breed
        FROM (
            SELECT name, age, breed
            FROM dogs
            ORDER BY age DESC
            LIMIT 4
        )
        ORDER BY breed ASC;
    """, conn)
    conn.close()
    return df


# PART 4: BABE RUTH DATABASE

def step9_total_years():
    conn = sqlite3.connect("babe_ruth.db")
    df = pd.read_sql("""
        SELECT COUNT(year) AS total_years
        FROM babe_ruth_stats;
    """, conn)
    conn.close()
    return df


def step10_total_home_runs():
    conn = sqlite3.connect("babe_ruth.db")
    df = pd.read_sql("""
        SELECT SUM(HR) AS total_home_runs
        FROM babe_ruth_stats;
    """, conn)
    conn.close()
    return df


def step11_team_years():
    conn = sqlite3.connect("babe_ruth.db")
    df = pd.read_sql("""
        SELECT team, COUNT(year) AS number_years
        FROM babe_ruth_stats
        GROUP BY team;
    """, conn)
    conn.close()
    return df


def step12_avg_at_bats():
    conn = sqlite3.connect("babe_ruth.db")
    df = pd.read_sql("""
        SELECT team, AVG(AB) AS average_at_bats
        FROM babe_ruth_stats
        GROUP BY team
        HAVING AVG(AB) > 200;
    """, conn)
    conn.close()
    return df