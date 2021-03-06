import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='activecampaign-python',
      version='1.0.0',
      description='ActiveCampaign API written in python',
      long_description=read('README.md'),
      author='Miguel Ferrer',
      author_email='ingferrermiguel@gmail.com',
      url='https://github.com/GearPlug/activecampaign-python',
      packages=['activecampaign'],
      install_requires=[
          'requests',
      ],
      keywords='activecampaign',
      zip_safe=False,
      license='MIT',
      )
