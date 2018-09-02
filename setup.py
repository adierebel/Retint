from importlib.machinery import SourceFileLoader
from setuptools import setup

version = SourceFileLoader('version', 'retint/version.py').load_module()

setup(
	name='retint',
	version=str(version.VERSION),
	description='Android icon tinting',
	long_description='Android icon tinting',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Console',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Intended Audience :: Developers',
		'Intended Audience :: Information Technology',
		'Intended Audience :: System Administrators',
		'License :: OSI Approved :: MIT License',
		'Operating System :: Unix',
		'Operating System :: POSIX :: Linux',
		'Environment :: MacOS X',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
	author='Adierebel',
	author_email='adierebel@gmail.com',
	url='https://github.com/adierebel/retint',
	entry_points="""
		[console_scripts]
		retint=retint.main:cli
	""",
	install_requires=[
		'click==6.7',
		'Pillow==5.2.0'
	],
	license='MIT',
	packages=['retint'],
	python_requires='>=3.5',
	zip_safe=True,
)