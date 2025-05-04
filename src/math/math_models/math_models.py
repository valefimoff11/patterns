def population_growth(initial_population, growth_rate, years):
    return initial_population * (1 + growth_rate) ** years

population = 1000
annual_rate = 0.05

projection = population_growth(population, annual_rate, 10)
print(f"Population after 10 years: {projection}")

def compound_interest(principal, rate, time_period, compounds_per_year):

    compound_interest = principal * (1 + rate/compounds_per_year) ** (compounds_per_year * time_period)

    return compound_interest

initial_investment = 1000
interest_rate = 0.08
years = 5
compounds_per_year = 12
result = compound_interest(initial_investment, interest_rate, years, compounds_per_year)

print(f"Total value: {result:.2f}")

