    from setuptools import setup, find_packages

    setup(
        name='WebDataScraper',
        version='0.1.0',
        author='Harmanpreet Singh',
        author_email='your.email@example.com',
        description='A short description of your package',
        long_description=open('README.md').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/comdotharman0/WebDataScraper',
        packages=find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
        ],
        python_requires='>=3.6',
        install_requires=[
          requests,beautifulsoup4
            # List your dependencies here, e.g., 'requests>=2.20.0'
        ],
    )
