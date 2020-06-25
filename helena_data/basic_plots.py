from argparse import ArgumentParser

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from import_data import load_csv
#Set Default Figure size
sns.set(rc={'figure.figsize':(11,4)})

import pdb

def label_plot(title: str = None, xlabel: str = None, ylabel: str = None):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

def build_cols_to_remove(cols_to_keep):
    '''From the full list of columns, filter out the columns to keep'''
    COLUMNS = ['leftDuration', 'rightDuration', 'bottleVolume', 'pee', 'poo', 'sleepDuration', 'weight', 'note']
    cols_to_remove = [col for col in COLUMNS if col not in cols_to_keep]
    return cols_to_remove

def single_column_data(baby_data: pd.DataFrame, col: str) -> pd.DataFrame:
    '''Extract a single column of data from the baby_data
       Returns a data frame object with just the single column'''
    cols_to_keep = [col]
    to_remove = build_cols_to_remove(cols_to_keep)
    data = baby_data[baby_data[col].notnull()].drop(columns=to_remove)
    return data

def single_column_plot(baby_data: pd.DataFrame, col: str, plot_kind: str, show_plot: bool = False, title: str = None, xlabel: str = None, ylabel: str = None):
    '''Plot col from the baby_data using plot_type kind of plot
       Returns a tuple (plot_data, plot)'''
    data = single_column_data(baby_data, col)
    plot = data[col].plot(kind=plot_kind)
    label_plot(title=title, xlabel=xlabel, ylabel=ylabel)
    if (show_plot):
        plt.show()
    return (data, plot)

def plot_weight(baby_data: pd.DataFrame, show_plot=False):
    '''Plot weight over time in this data frame'''
    return single_column_plot(baby_data, col='weight', plot_kind='line', show_plot=show_plot, title='Weight over Time', xlabel='Time', ylabel='Weight (g)')

def plot_bottle_volume_per_day(baby_data: pd.DataFrame, show_plot=False):
    '''Plot the amount consumed from a bottle each day as a bar chart'''
    bottle_data = single_column_data(baby_data, 'bottleVolume')
    bottle_daily = bottle_data.groupby(bottle_data.index.date).sum()
    bottle_plot = bottle_daily['bottleVolume'].plot(kind='bar')
    label_plot(title='Bottle Volume Drank Each Day', xlabel='Date', ylabel='Volume (ml)')
    if(show_plot):
        plt.show()
    return (bottle_daily, bottle_plot)

def plot_poos_per_day(baby_data: pd.DataFrame, show_plot=False):
    '''Plot the number of diapers changed each day with poo'''
    poo_data = single_column_data(baby_data, 'poo')
    poo_daily = poo_data.groupby(poo_data.index.date).sum()
    poo_plot = poo_daily['poo'].plot(kind='bar')
    label_plot(title='Poos Per Day', xlabel='Date', ylabel='# of Poos')
    if(show_plot):
        plt.show()
    return (poo_daily, poo_plot)


def plot_pees_per_day(baby_data: pd.DataFrame, show_plot=False):
    '''Plot the number of diapers changed each day with pee'''
    pee_data = single_column_data(baby_data, 'pee')
    pee_daily = pee_data.groupby(pee_data.index.date).sum()
    pee_plot = pee_daily['pee'].plot(kind='bar')
    label_plot(title='Pees Per Day', xlabel='Date', ylabel='# of Pees')

    if(show_plot):
        plt.show()
    return (pee_daily, pee_plot)

def plot_sleep_per_day(baby_data: pd.DataFrame, show_plot=False):
    '''Plot the number of diapers changed each day with sleep'''
    sleep_data = single_column_data(baby_data, 'sleepDuration')
    sleep_daily = sleep_data.groupby(sleep_data.index.date).sum()
    sleep_plot = sleep_daily['sleepDuration'].plot(kind='bar')
    label_plot(title='Sleep Per Day', xlabel='Date', ylabel='Sleep (s)')

    if(show_plot):
        plt.show()
    return (sleep_daily, sleep_plot)

def growth_per_day(baby_data: pd.DataFrame):
    '''Generate a dataframe that has two columns. One that is the data, and one that is the growth that happened that day
       If no weight measurement was made that day, interpolate the growth with a linear interpolation of the surrounding days
    '''


def main():
    parser = ArgumentParser(description=__file__)
    parser.add_argument('--csv',
                        help='CSV file outputted from LeBaby to be processed',
                        required=True)
    args = parser.parse_args()
    print(f"Processing {args.csv} ...")

    baby_data = load_csv(args.csv)

    plot_weight(baby_data, show_plot=True)
    plot_bottle_volume_per_day(baby_data, show_plot=True)
    plot_poos_per_day(baby_data, show_plot=True)
    plot_pees_per_day(baby_data, show_plot=True)
    plot_sleep_per_day(baby_data, show_plot=True)

if __name__ == '__main__':
    main()

