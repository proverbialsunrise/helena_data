import pandas

def load_csv(filename: str):
    '''Loads the file specified and returns a pandas dataframe'''
    baby_df = pd.read_csv(filename, index_col=0, parse_dates=True)
    return baby_df

if __name__ == "__main__":
    # execute only if run as a script
    dataframe = load_csv('../data/x-small.csv')
    print(dataframe)
