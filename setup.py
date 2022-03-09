import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='rmk_swarm',                           # should match the package folder
    packages=['rmk_swarm'],                     # should match the package folder
    version='v0.0.1-alpha',                                # important for updates
    license='MIT',                                  # should match your chosen license
    description='Package for Helping Swarm Intelligence Modeling',
    long_description=long_description,              # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='Riksa Meidy Karim',
    author_email='riksameidy@gmail.com',
    url='https://github.com/riksameidy/rmk_swarm', 
    install_requires=['requests'],                  # list all packages that your package uses
    keywords=["pypi", "rmk_swarm", "Swarm"], #descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    
    download_url="https://github.com/riksameidy/rmk_swarm/archive/refs/tags/v0.0.1-alpha.tar.gz",
)
