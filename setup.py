from setuptools import setup, find_packages

# Odd hack to get tests running smoothly on py2.7
try:
    import multiprocessing
    import logging
except:
    pass

setup(
    name='tw2.jqplugins.select2',
    version='0.1.4',
    description='ToscaWidgets 2 SelectFields enhanced with the select2 javascript library.',
    long_description=open('README.md').read(),
    author='Ralph Bean',
    author_email='rbean@redhat.com',
    url='https://github.com/toscawidgets/tw2.jqplugins.select2',
    license='MIT',
    install_requires=[
        "tw2.core",
        "tw2.forms",
        "tw2.jquery",
        ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages = ['tw2'],
    zip_safe=False,
    include_package_data=True,
    tests_require = [
        'nose',
        'BeautifulSoup',
        'FormEncode',
        'WebTest',
        'strainer',

        'mako',
        'genshi',
    ],
    test_suite = 'nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.jqplugins.select2
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
