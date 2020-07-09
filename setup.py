
from setuptools import find_packages, setup


setup(
    name='noaapy',
    version='0.5.0',
    author='Aaron Schlegel',
    author_email='aaron@aaronschlegel.me',
    url='https://github.com/aschleg/petpy',
    description='Wrapper for the National Centers for Environmental Information API',
    license='MIT',
    packages=find_packages(exclude=['build', 'dist', 'petpy.egg-info',
                                    'docs', 'notebooks', 'tests*']),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['requests>=2.18.4'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)