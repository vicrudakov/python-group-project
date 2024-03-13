import seaborn as sns
import matplotlib.pyplot as plt


class VisualizeWineData:
    def __init__(self, data):
        """Visualize wine data using histograms and boxplots.

        Parameters
        ----------
        data : pandas.core.frame.DataFrame
            Downloaded wine dataset.

        Returns
        -------
        None.
        """
        self.data = data
        self.var_names = ['Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols',
                          'Flavanoids', 'Nonflavanoid\nphenols', 'Proanthocyanins', 'Color intensity', 'Hue',
                          'OD280/OD315 of\ndiluted wines', 'Proline']

    def __call__(self):
        self.draw_histograms()
        self.draw_boxplots()

    def draw_histograms(self):
        """Draw histograms with additional boxplots for each feature in the dataset ('class', 'alcohol', 'malic_acid',
        'ash', 'ash_alcalinity', 'magnesium', 'phenols_total', 'flavanoids', 'phenols_nonflavanoid', 'proanthocyanins',
        'color_intensity', 'hue', 'OD280_OD315', 'proline').

        Parameters
        ----------
        None.

        Returns
        -------
        matplotlib.plot

        """
        # create an empty figure
        plt.figure()

        # create axes for the third row
        fig, axes1 = plt.subplots(3, 7, figsize=(15, 20), width_ratios=[1, 2, 1, 2, 1, 2, 1])
        axes1 = axes1.flatten()
        for i in range(len(axes1)):
            if i not in [15, 17, 19]:
                axes1[i].remove()

        # create axes for first and second row
        axes2 = []
        for i in range(1, 11):
            axes2.append(plt.subplot(3, 5, i))

        # combine all axes
        axes2.append(axes1[15])
        axes2.append(axes1[17])
        axes2.append(axes1[19])

        # adjust spaces between plots
        fig.subplots_adjust(hspace=0.3, wspace=0.5, top=0.93)

        # add title to the plot
        fig.suptitle("Histograms and boxplots for each feature in the dataset")

        # draw histograms
        for i, column in enumerate(self.data.columns[1:len(self.data.columns)]):
            ax = axes2[i]

            # Create histogram and get counts
            hist_data = sns.histplot(y=self.data[column], bins=30, kde=True, alpha=0.7, ax=ax)
            counts = [p.get_width() for p in hist_data.patches]

            # Set title and labels
            ax.set_title(self.var_names[i])
            ax.set_xlabel("Frequency")
            ax.set_ylabel("Value")
            ax.set_xticks(ax.get_xticks())

            # Create boxplot with fixed width
            ax_box = ax.twinx()
            ax.boxplot(self.data[column], vert=True, widths=(max(counts) - min(counts)) * 0.07,
                       patch_artist=True, boxprops=dict(facecolor='white'), manage_ticks=False)
            ax_box.set_yticks([])

        return (fig, axes2)

    def draw_boxplots(self):
        """Draw boxplots for each feature in the dataset ('class', 'alcohol', 'malic_acid',
        'ash', 'ash_alcalinity', 'magnesium', 'phenols_total', 'flavanoids', 'phenols_nonflavanoid', 'proanthocyanins',
        'color_intensity', 'hue', 'OD280_OD315', 'proline') separated by class.

        Parameters
        ----------
        None.

        Returns
        -------
        matplotlib.plot

        """
        # create an empty figure
        plt.figure()

        # create axes for the third row
        fig, axes1 = plt.subplots(3, 7, figsize=(10, 10), width_ratios=[1, 2, 1, 2, 1, 2, 1])
        axes1 = axes1.flatten()
        for i in range(len(axes1)):
            if i not in [15, 17, 19]:
                axes1[i].remove()

        # create axes for first and second row
        axes2 = []
        for i in range(1, 11):
            axes2.append(plt.subplot(3, 5, i))

        # combine all axes
        axes2.append(axes1[15])
        axes2.append(axes1[17])
        axes2.append(axes1[19])
        
        # adjust spaces between plots
        fig.subplots_adjust(hspace=0.6, wspace=0.7, top=0.9)
        
        # add title to the plot
        fig.suptitle("Boxplots for each feature in the dataset separated by class")

        # draw boxplots
        for i, column in enumerate(self.data.columns[1:len(self.data.columns)]):
            ax = axes2[i]
            sns.boxplot(x='class', y=column, data=self.data, ax=ax, hue='class')
            ax.set_title(self.var_names[i])
            ax.set_xlabel('Class')
            ax.set_ylabel('Value')
            ax.get_legend().set_visible(False)

        return (fig, axes2)