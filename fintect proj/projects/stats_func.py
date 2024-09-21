

def long_tail(df):
    try:
        three_years_peak = max(df.iloc[:1000,:].High)
        two_years_low = min(df.iloc[600:, :].Low)
    except:
        return False
    if three_years_peak/two_years_low > 15:
        return True
    else:
        return False