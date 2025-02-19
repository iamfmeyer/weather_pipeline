"""Base collector implementation"""

from abc import ABC, abstractmethod
from typing import Any, Dict
from loguru import logger


class BaseCollector(ABC):
    """
    Abstract base class for all collectors
    """

    def __init__(self) -> None:
        self.logger = logger.bind(collector=self.__class__.__name__)

    @abstractmethod
    def collect(self, **args) -> Dict[str, Any]:
        """
        Abstract method to collect data

        Args:
            **kwargs: Arbitrary keyword arguments needed for collection

        Returns:
            Dict[str, Any]: Dict containing collected data
        """
        pass

    def _validate_response(self, data: Dict[str, Any]) -> bool:
        """
        Validate the collected data

        Args:
            data (Dict[str, Any]): The data to validate

        Returns:
            bool: True if valid, False otherwise
        """
        return bool(data)
