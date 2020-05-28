from setuptools import setup, find_packages


setup(
    name="convolutonal_neural_network",
    version='1.0',
    description='HAL東京RO14の課題制作で使用した畳みこみニューラルネットワーク',
    author='Ryuya Saito',
    author_email='saitoryuya945@gmail.com',
    url='https://github.com/SaitoRyuya945/convolutonal_neural_network',
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        convolutonal_neural_network = convolutonal_neural_network.cli.execute
    """,
)
