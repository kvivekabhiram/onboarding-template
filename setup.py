from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(name='onboarding',
      version='0.001',
      description='Introductory role to help familiarize newly onboarded engineers',
      long_description=readme,
      author='Dom DeGuzman',
      author_email='dom@twilio.com',
      packages=find_packages())
