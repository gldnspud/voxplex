"""
VoxPlex synchronizes files to/from SunVox for iOS
"""
from setuptools import find_packages, setup

dependencies = ['click', 'prompt-toolkit', 'pyquery', 'pyyaml', 'requests']

setup(
    name='voxplex',
    version='0.1.0',
    url='https://github.com/gldnspud/voxplex',
    license='BSD',
    author='Matthew Scott',
    author_email='matt@11craft.com',
    description='VoxPlex synchronizes files to/from SunVox for iOS',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'voxplex = voxplex.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
