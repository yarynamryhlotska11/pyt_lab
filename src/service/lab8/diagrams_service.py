from collections import Counter
import abc
from matplotlib import pyplot as plt
from configuration.logger_config import logger
from domain.lab8.user import User
from shared.data_processor import DateProcessor
from shared.file_processors import CsvProcessor as csv_processor
from shared.json_utility import read_json_file


class DiagramService(abc.ABC):
    def __init__(self):
        self._users = []


class DiagramServiceImpl(DiagramService):

    def __init__(self, file_path: str):
        super().__init__()
        users_dataframe = csv_processor.read(file_path)
        for data in users_dataframe.values:
            self._users.append(User(data))

    def get_state(self):
        return [user.state for user in self._users]

    def get_sex(self):
        return [user.sex for user in self._users]

    def get_job_title(self):
        logger.info("Retrieving job titles")
        return [user.job_title for user in self._users]

    def create_states_histogram(self, has_to_be_downloaded=False):
        state = self.get_state()
        state_counter = Counter(state)

        plt.figure(figsize=(8, 7))
        plt.bar([key for key in state_counter], [state_counter[key] for key in state_counter],
                color='green')

        json_data = read_json_file(file_path="../src/configuration/paths_config.json")
        if has_to_be_downloaded:
            plt.savefig(json_data["STATES_HISTOGRAM"])

        plt.title('Bar Chart')
        plt.xlabel('States')
        plt.ylabel('Frequency')
        plt.xticks(fontsize=6)
        plt.yticks(fontsize=10)
        plt.xticks(rotation=-90)

        plt.show()

    def create_pie_chart(self, has_to_be_downloaded: False):
        state = self.get_state()
        state_counter = Counter(state)
        max_quantity: int = 10
        sorted_dict_values = dict(sorted(state_counter.items(), key=lambda item: item[1], reverse=True)[:max_quantity])

        labels = list(sorted_dict_values.keys())
        sizes = list(sorted_dict_values.values())

        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

        json_data = read_json_file(file_path="../src/configuration/paths_config.json")
        if has_to_be_downloaded:
            plt.savefig(json_data["PIE_CHART_PHOTO"])

        plt.title('Pie Chart')
        plt.show()

    def create_combined_diagram(self, has_to_be_downloaded=False):
        state = self.get_state()
        state_counter = Counter(state)
        max_quantity: int = 10
        sorted_dict_values = dict(sorted(state_counter.items(), key=lambda item: item[1], reverse=True)[:max_quantity])
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

        # Bar Chart
        ax1.bar([key for key in state_counter], [state_counter[key] for key in state_counter], color='green')
        ax1.set_title('Bar Chart')
        ax1.set_xlabel('States')
        ax1.set_ylabel('Frequency')
        ax1.tick_params(axis='x', rotation=45)  # Adjust rotation if needed

        labels = list(sorted_dict_values.keys())
        sizes = list(sorted_dict_values.values())
        ax2.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax2.set_title('Pie Chart')

        # Adjust layout
        plt.tight_layout()

        json_data = read_json_file(file_path="../src/configuration/paths_config.json")
        if has_to_be_downloaded:
            plt.savefig(json_data["COMBINED_DIAGRAM_PHOTO"])

        plt.show()
