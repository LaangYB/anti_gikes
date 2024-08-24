from setuptools import setup, find_packages

setup(
    name="anti_gikes",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Daftar dependensi yang ada di requirements.txt
    ],
    entry_points={
        'console_scripts': [
            'antigikes=main:main',  # Misal: antikata = nama_modul:fungsi_utama
        ],
    },
)
