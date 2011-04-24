from distutils.core import setup

setup(
    name='django-cuit',
    version='0.1.dev',
    author='Ivan Raskovsky (rasca)',
    author_email='raskovsky@gmail.com',
    packages=['cuit',],
    license='BSD',
    description='django app for verification of Argentinian AFIP CUITs',
    long_description=open('README.rst').read(),
    keywords = 'django ar cuit afip',
    url = 'http://github.com/rasca/django-cuit',
    install_requires = ['Django>=1.0'],
)
