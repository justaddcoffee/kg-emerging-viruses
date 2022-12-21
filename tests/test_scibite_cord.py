"""Tests for parsing Scibite CORD data."""

import tempfile
from unittest import TestCase

from kg_covid_19.transform_utils.scibite_cord import ScibiteCordTransform


class TestScibiteCord(TestCase):
    """Test for parsing Scibite CORD data."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up the test class."""
        cls.input_dir = "tests/resources/scibite_cord"
        cls.output_dir = "tests/resources/scibite_cord"
        cls.tmpdir = tempfile.TemporaryDirectory(dir=cls.input_dir)
        cls.scibite = ScibiteCordTransform(
            input_dir=cls.input_dir, output_dir=cls.tmpdir.name
        )

    def test_run(self):
        """Test running the scibite transformation."""
        self.scibite.run()
