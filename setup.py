from setuptools import setup

setup(name='threeiesms',
      version='0.1',
      description='Sends sms through Three(IE) webtext.',
      url='http://github.com/niallbunting/threeiesms',
      author='Niall Bunting',
      author_email='',
      license='MIT',
      packages=['threeiesms'],
      install_requires=[
          'requests',
      ],
      zip_safe=False,
      entry_points={
        'console_scripts': ['threeiesms=threeiesms.shell:main'],
      }
)
