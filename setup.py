from setuptools import setup, find_packages

setup(
    name='newsfacts',
    version='0.1',
    description="Tracking the numbers behind the news.",
    long_description='',
    classifiers=[
        ],
    keywords='fact-checking stories numbers journalism ddj',
    author='Open Knowledge Foundation',
    author_email='info@okfn.org',
    url='http://okfn.org',
    license='AGPLv3',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        'sqlalchemy==0.7.8',
        'Flask==0.9',
        'Flask-Script==0.3.3',
        'flask-sqlalchemy==0.16',
        'Unidecode==0.04.9',
        'SQLAlchemy==0.7.8',
        'python-dateutil==2.0',
        'feedparser==5.1.2',
        'lxml==2.3.4',
        'python-dateutil==2.0',
        'requests==0.13.2'
    ],
    tests_require=[],
    entry_points=\
    """ """,
)
