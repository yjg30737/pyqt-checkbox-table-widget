from setuptools import setup, find_packages

setup(
    name='pyqt-checkbox-table-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt\'s QTableWidget which has checkbox as first header item',
    url='https://github.com/yjg30737/pyqt-checkbox-table-widget.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)