from setuptools import setup

setup(name='cavaconn',
      version='0.1',
      description='Create database engines for SQL servers, and easily connect to APIs',
      url='https://github.com/cavagrill/cavaconn',
      download_url='https://github.com/cavagrill/cavaconn/tarball/0.1',
      author='Jordan Bramble',
      author_email='jordan.bramble@cavagrill.com',
      license='MIT',
      packages=['cavaconn'],
      install_requires=['psycopg2', 'PyYAML', 'sqlalchemy', 'pymssql'],
      zip_safe=False)
