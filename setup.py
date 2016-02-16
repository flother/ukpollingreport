from setuptools import setup, find_packages


setup(
    name         = "ukpollingreport",
    version      = "1.0.0",
    packages     = find_packages(),
    entry_points = {"scrapy": ["settings = ukpollingreport.settings"]},
)
