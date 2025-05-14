s = pl.Series(["2020-01-01 01:00Z", "2020-01-01 02:00Z"])
s.str.to_datetime("%Y-%m-%d %H:%M%#z")