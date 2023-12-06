import abc
from src.utility.FileProcessor import CsvProcessor as csv_processor
from consumer import Consumer
from matplotlib import pyplot as plt
from collections import Counter


@abc.abstractmethod
class ConsumerService(abc.ABC):

    def __init__(self):
        self._consumers = []


class ConsumerServiceImpl(ConsumerService):
    def __init__(self, file_path: str):
        super().__init__()
        consumers_dataframe = csv_processor.read(file_path)
        for data in consumers_dataframe.values:
            self._consumers.append(Consumer(data))

    def get_states(self):
        return [consumer.state for consumer in self._consumers]

    def create_states_histogram(self, has_to_be_downloaded: bool):
        states = self.get_states()
        state_counter = Counter(states)

        plt.figure(figsize=(8, 7))
        plt.bar([key for key in state_counter], [state_counter[key] for key in state_counter],
                color='green')

        if has_to_be_downloaded:
            plt.savefig('./files/state-bar-chart.png')
        plt.title('Bar Chart')
        plt.xlabel('States')
        plt.ylabel('Frequency')
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=10)
        plt.xticks(rotation=-90)

        plt.show()

    def create_states_pie_chart(self, has_to_be_downloaded: bool, max_quantity: int = 10):
        states = self.get_states()
        state_counter = Counter(states)
        sorted_dict_values = dict(sorted(state_counter.items(), key=lambda item: item[1], reverse=True)[:max_quantity])

        labels = list(sorted_dict_values.keys())
        sizes = list(sorted_dict_values.values())

        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

        if has_to_be_downloaded:
            plt.savefig('./files/state-pie-chart.png')

        plt.title('Pie Chart')
        plt.show()

    def create_combined_diagram(self, has_to_be_downloaded: bool, max_quantity: int = 10):
        states = self.get_states()
        state_counter = Counter(states)
        sorted_dict_values = dict(sorted(state_counter.items(), key=lambda item: item[1], reverse=True)[:max_quantity])

        # Create a figure with two subplots: one for the bar chart and one for the pie chart
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

        # Bar Chart
        ax1.bar([key for key in state_counter], [state_counter[key] for key in state_counter], color='green')
        ax1.set_title('Bar Chart')
        ax1.set_xlabel('States')
        ax1.set_ylabel('Frequency')
        ax1.tick_params(axis='x', rotation=45)  # Adjust rotation if needed

        # Pie Chart
        labels = list(sorted_dict_values.keys())
        sizes = list(sorted_dict_values.values())
        ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax2.set_title('Pie Chart')

        # Adjust layout
        plt.tight_layout()

        # Save or show the plot
        if has_to_be_downloaded:
            plt.savefig('./files/combined-chart.png')
        plt.show()
