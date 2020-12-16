# check file
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot():
    #read data from file into a panda
    df = pd.read_pickle('data_file.pkl')

    columns = list(df)

    # convert categoric answers from strings to categorical variable
    for i in columns[:-1]:
        if isinstance(df[i][0], str):
            df[i] = pd.Categorical(df[i], categories=["yes", "no"])

    #boxplot for Happiness and Friends
    fig, axs = plt.subplots(nrows=2, ncols=3)
    axs[0][0].boxplot([df['Happiness'][df['Friends'] == 'yes'], df['Happiness'][df['Friends'] == 'no']])
    axs[0][0].set_xlabel('Friends')
    axs[0][0].set_ylabel('Happiness')
    axs[0][0].set_xticks([1, 2])
    axs[0][0].set_xticklabels(["yes", "no"])

    #boxplot for Happiness and Alcohol
    axs[0][1].boxplot([df['Happiness'][df['Alcohol'] == 'yes'], df['Happiness'][df['Alcohol'] == 'no']])
    axs[0][1].set_xlabel('Alcohol')
    axs[0][1].set_ylabel('Happiness')
    axs[0][1].set_xticks([1, 2])
    axs[0][1].set_xticklabels(["yes", "no"])

    #boxplot for Happiness and Sport
    axs[0][2].boxplot([df['Happiness'][df['Sport'] == 'yes'], df['Happiness'][df['Sport'] == 'no']])
    axs[0][2].set_xlabel('Sport')
    axs[0][2].set_ylabel('Happiness')
    axs[0][2].set_xticks([1, 2])
    axs[0][2].set_xticklabels(["yes", "no"])

    #boxplot for Hapiness and Warm Meal
    axs[1][0].boxplot([df['Happiness'][df['Warm Meal'] == 'yes'], df['Happiness'][df['Warm Meal'] == 'no']])
    axs[1][0].set_xlabel('Warm Meal')
    axs[1][0].set_ylabel('Happiness')
    axs[1][0].set_xticks([1, 2])
    axs[1][0].set_xticklabels(["yes", "no"])

    #boxplot for Hapiness and Pleasure
    axs[1][1].boxplot([df['Happiness'][df['Pleasure'] == 'yes'], df['Happiness'][df['Pleasure'] == 'no']])
    axs[1][1].set_xlabel('Pleasure')
    axs[1][1].set_ylabel('Happiness')
    axs[1][1].set_xticks([1, 2])
    axs[1][1].set_xticklabels(["yes", "no"])

    #boxplot for Hapiness and Success Experience
    axs[1][2].boxplot([df['Happiness'][df['Success Experience'] == 'yes'], df['Happiness'][df['Success Experience'] == 'no']])
    axs[1][2].set_xlabel('Success Experience')
    axs[1][2].set_ylabel('Happiness')
    axs[1][2].set_xticks([1, 2])
    axs[1][2].set_xticklabels(["yes", "no"])

    # print the plot to console
    plt.show()

    #make a pair plot of all continuous data
    sns.pairplot(data=df)
    plt.show()
