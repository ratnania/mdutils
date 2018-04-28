from setuptools import setup

setup(name='mdutils',
      version=1.0,
      license='MIT',
      author='Didac Coll',
      author_email='didaccoll_93@hotmail.com',
      maintainer='Dídac Coll',
      maintainer_email='didaccoll_93@hotmail.com',
      description='A package, useful to create Markdown files while executing python code.',
      long_description=open('README.md').read(),
      platforms=['Python 3.6'],
      packages=['mdutils', 'mdutils.tools', 'mdutils.fileutils'],
      include_package_data=True,
      zip_safe=False,
      url='https://github.com/didix21/mdutils',
      classifiers=['Development Status :: 4 - Beta',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Utilities',
                   'Topic :: Software Development :: Documentation',
                   'License :: OSI Approved :: MIT License'])
