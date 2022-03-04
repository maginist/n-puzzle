from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

requirements = [
    "pandas==1.3.4",
    "numpy==1.21.4",
    "progress==1.6",
    "matplotlib==3.5.1",
    "seaborn==0.11.2",
]

test_requirements = ["pytest==6.2.5"]
dev_requirements = ["black==21.10b0"] + test_requirements

extra_requirements = {
    "dev": dev_requirements,
}

setup(
    name="n-puzzle",
    version="0.0.1",
    description="The goal of this project is to solve the N-puzzle game using the A* search algorithm",
    long_description=long_description,
    author="Mathieu Ginisty, Malo Boucé",
    author_email="maginist@student.42.fr",
    url="https://github.com/maginist/n-puzzle.git",
    packages=["tests", "n_puzzle"],
    entry_points={
        "console_scripts": [
            "n_puzzle = n_puzzle.n_puzzle:cli",
            # SCRIPTS
            "generate_puzzle = n_puzzle.scripts.generate_puzzle:cli",
            # END OF SCRIPTS
        ],
    },
    install_requires=requirements,
    extras_require=extra_requirements,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
