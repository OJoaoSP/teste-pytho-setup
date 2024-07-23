from setuptools import setup, find_packages
setup(
    name='printer',
    version='0.8.0',
    description='Descrição do seu pacote',
    packages=find_packages(where='printer_teste'),
    python_requires='>=3.9',
    setup_requires=['setuptools'],
    entry_points={
        'console_scripts': [
            'create_tar_gz=setup:create_tar_gz',
        ]
    },
)
