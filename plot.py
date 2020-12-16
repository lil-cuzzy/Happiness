# check file
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot():
    sns.set_style(style="whitegrid")
    df = pd.read_pickle('data_file.pkl')
    print(df.head(5))

    columns = list(df)

    for i in columns[:-1]:
        if isinstance(df[i][0], str):
            df[i] = pd.Categorical(df[i], categories=["yes", "no"])
    print(df.head(5))
    fig, axs = plt.subplots(nrows=2, ncols=3)
    axs[0][0].boxplot([df['Happiness'][df['Friends'] == 'yes'], df['Happiness'][df['Friends'] == 'no']])
    axs[0][0].set_xlabel('Friends')
    axs[0][0].set_ylabel('Happiness')
    axs[0][0].set_xticks([1, 2])
    axs[0][0].set_xticklabels(["yes", "no"])
    # TODO add axis and label
    axs[0][1].boxplot([df['Happiness'][df['Alcohol'] == 'yes'], df['Happiness'][df['Alcohol'] == 'no']])
    # TODO remove depriciation warning
    axs[0][2].boxplot([df['Happiness'][df['Sport'] == 'yes'], df['Happiness'][df['Sport'] == 'no']])
    axs[1][0].boxplot([df['Happiness'][df['Warm Meal'] == 'yes'], df['Happiness'][df['Warm Meal'] == 'no']])

    axs[1][1].boxplot([df['Happiness'][df['Pleasure'] == 'yes'], df['Happiness'][df['Pleasure'] == 'no']])

    axs[1][2].boxplot(
        [df['Happiness'][df['Success Experience'] == 'yes'], df['Happiness'][df['Success Experience'] == 'no']])

    plt.show()

    scalar_data = df[["Happiness", "Sleep", "Work", "Outdoor"]]
    sns.heatmap(scalar_data)
    plt.show()
    sns.pairplot(data=df)
    plt.show()
