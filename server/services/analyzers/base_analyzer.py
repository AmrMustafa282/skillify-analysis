"""
Base analyzer class for all analyzers.
"""
from typing import Dict, Any, List
from abc import ABC, abstractmethod


class BaseAnalyzer(ABC):
    """Base class for all analyzers."""

    @abstractmethod
    def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze the data and return the results.

        Args:
            data: Data to analyze

        Returns:
            Analysis results
        """
        pass


class AnalyzerPipeline:
    """Pipeline for running multiple analyzers in sequence."""

    def __init__(self, analyzers: List[BaseAnalyzer]):
        """Initialize the pipeline with a list of analyzers.

        Args:
            analyzers: List of analyzers to run
        """
        self.analyzers = analyzers

    def run(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Run all analyzers in the pipeline.

        Args:
            data: Data to analyze

        Returns:
            Combined analysis results
        """
        results = {}
        
        for analyzer in self.analyzers:
            analyzer_result = analyzer.analyze(data)
            results.update(analyzer_result)
        
        return results
