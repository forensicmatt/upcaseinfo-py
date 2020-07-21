from setuptools import setup


setup(
    name='upcaseinfo',
    version="0.1.0",
    description='Library and tools to parse $Upcase:$Info.',
    author='Matthew Seyer',
    packages=[
        "upcaseinfo",
    ],
    install_requires=[],
    scripts=[
        'scripts/upcaseinfo_parser.py',
    ]
)

