from setuptools import setup

setup(name='paction',
      version='0.1',
      description='Preforms a Protected ACTION.',
      url='http://github.com/niallbunting/paction',
      author='Niall Bunting',
      author_email='',
      license='MIT',
      packages=['paction'],
      install_requires=[
          'requests',
      ],
      zip_safe=False,
      entry_points={
        'console_scripts': ['paction=paction.shell:main'],
      }
)
