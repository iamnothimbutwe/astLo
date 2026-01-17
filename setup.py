from setuptools import setup

setup(
    name="astlo",
    version="0.1.2",
    description="Orbital mechanics engine for planetary calculations",
    author="iamnothimbutwe/Mark",
    py_modules=["astlo"], # This points to astlo.py
    install_requires=[
        "plotext",'rich','click'# Any external library you use
    ],
    entry_points={
        'console_scripts': [
            'astlo=astlo:main', # This creates the 'astlo' command
        ],
    },
)

