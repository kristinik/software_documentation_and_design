from output.console_strategy import ConsoleOutputStrategy
from output.kafka_strategy import KafkaOutputStrategy


class OutputFactory:
    @staticmethod
    def create_output_strategy(config):
        output_type = config["output"]["type"]

        if output_type == "console":
            return ConsoleOutputStrategy()

        if output_type == "kafka":
            kafka_config = config["kafka"]

            return KafkaOutputStrategy(
                bootstrap_servers=kafka_config["bootstrap_servers"],
                topic=kafka_config["topic"]
            )

        raise ValueError(f"Невідомий тип виводу: {output_type}")