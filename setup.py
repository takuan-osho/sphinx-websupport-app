from setuptools import setup, find_packages

setup(
    name="sphinxweb",
    version="0.1.0",
    url='https://github.com/shimizukawa/sphinx-websupport-app',
    author="Jacob Mason",
    author_email="noreply@example.org",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-OpenID',
        'Flask-Mail',
        'Flask-OAuthlib',
        'SQLAlchemy',
        'Sphinx',
    ],
    entry_points={
        'console_scripts': [
            'sphinxweb-build=sphinxweb.build:main',
            'sphinxweb-runserver=sphinxweb.runserver:main',
            'sphinxweb-make-moderator=sphinxweb.make_moderator:main',
        ]
    },
)
