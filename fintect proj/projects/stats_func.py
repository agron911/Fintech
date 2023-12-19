

def long_tail(df):
    three_years_peak = max(df.iloc[:1000,:].High)
    two_years_low = min(df.iloc[600:, :].Low)
    if three_years_peak/two_years_low > 15:
        return True
    else:
        return False