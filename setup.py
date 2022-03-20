from setuptools import find_packages, setup
from pathlib import Path

HERE = Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
	name="trading_platform",
	packages=find_packages(include=["trading_platform"], exclude=("tests",)),
	version="0.1.1",
	description="Trading platform SDK library",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/realpython/reader",
	author="Mihai Blebea",
	author_email="mihaiserban.blebea@gmail.com",
	license="MIT",
	install_requires=["requests"],
	setup_requires=["pytest-runner"],
	tests_require=["pytest==4.4.1"],
	test_suite="tests",
)