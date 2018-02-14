from setuptools import setup

setup(name='cavaconn',
      version='0.2',
      description='Create database engines for SQL servers, and easily connect to APIs',
      url='https://github.com/cavagrill/cavaconn',
      download_url='https://github.com/cavagrill/cavaconn/tarball/0.2',
      author='Jordan Bramble',
      author_email='tech@cava.com',
      license='MIT',
      packages=['cavaconn'],
      install_requires=['psycopg2-binary', 'PyYAML', 'sqlalchemy', 'pymssql'],
      zip_safe=False)
