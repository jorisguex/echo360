import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="echo360",
    version="2.0",
    description="Commandline tool for automated downloads of echo360 videos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soraxas/echo360",
    project_urls={
        "Documentation": "https://github.com/soraxas/echo360/blob/master/README.md",
        "Code": "https://github.com/soraxas/echo360",
        "Issue tracker": "https://github.com/soraxas/echo360/issues",
    },
    python_requires='>=2.7',
    install_requires=required,
    platforms='linux, macos, windows',
    entry_points={
    'console_scripts': [
        'echo360download=echo360.main:main',
        ],
        },
    package_data={'echo360': ['*.py']},
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Unix Shell",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
        "Topic :: System :: Networking",
        "License :: OSI Approved :: BSD License"
    ],
    license="BSD",
    author="soraxas",
    author_email="oscar@tinyiu.com"
)
