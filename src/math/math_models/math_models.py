def compound_interest(principal, rate, time_period, compounds_per_year):

    compound_interest = principal * (1 + rate/compounds_per_year) ** (compounds_per_year * time_period)

    return compound_interest

initial_investment = 1000
interest_rate = 0.08
years = 5
compouds_per_year = 12
result = compound_interest(initial_investment, interest_rate, years, compouds_per_year)

print(f"Total value: {result:.2f}")

