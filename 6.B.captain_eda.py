import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from sklearn.preprocessing import MinMaxScaler

def normalize_dates(df):
    scaler = MinMaxScaler(feature_range=(0, 100))
    each_hurricane = []
    df['date'] = pd.to_datetime(df['created_at'])
    hurricanes = df['hurricane'].unique()
    for h in hurricanes:
        df_s = df.where(df['hurricane'] == h).dropna()
        norm_dates = scaler.fit_transform(df_s['date'].values.reshape(-1,1))
        df_s['norm_date'] = norm_dates
        each_hurricane.append(df_s)
    df_normed = pd.concat(each_hurricane)
    return df_normed 

def all_kde(df):
    # kernel density estimate plot - all hurricanes
    ax_kde = sns.displot(
        data=df,
        x="norm_date", hue="class_label",
        kind="kde", height=5, aspect=1.5,
        multiple="fill", clip=(0, None)
    ).set(title='KDE plot_all hurricanes', xlabel='Time frame(0-100)', ylabel='Density')
    return ax_kde

def comparison(df):
    # kernel density estimate plot - by hurricane
    ax_kde_by_hurricanes = sns.displot(
        data=df,
        x="norm_date", col='hurricane', hue="class_label",
        kind="kde", height=4, aspect=1.5,
        multiple="fill", clip=(0, None), col_wrap=4
    ).set(xlabel='Time frame(0-100)', ylabel='Density').fig.suptitle('KDE plot_by hurricane', y=1.05)
    return ax_kde_by_hurricanes

def displot_(df):
    # facet grid with histograms - by hurricane
    d_plot = sns.displot(
        df, x="norm_date", col="hurricane", hue='class_label', multiple='stack', col_wrap=4,
        height=5, facet_kws=dict(margin_titles=True),
    ).set(xlabel='Time frame(0-100)', ylabel='Count').fig.suptitle('Histogram_by hurricane', y=1.05)
    return d_plot

def strip_box(df):
    # label boxplot overtime, all hurricanes
    f, ax = plt.subplots(figsize=(15, 6))
    box = sns.boxplot(x="norm_date", y="class_label", data=df,
                whis=[0, 100], width=.6, palette="vlag")
    strip = sns.stripplot(x="norm_date", y="class_label", data=df,
                  size=1, color=".3", linewidth=0)
    return box, strip
