import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012022S2LDO1',
      version='0.1.2',
      description=('A docassemble extension.'),
      long_description='# docassemble.LLAW33012022S2LDO1\r\n\r\nThis application produces the first draft in the amendment process for the Legislative Drafting Office of Jersey. Human inspection is necessary before publication. \r\n\r\n## Author\r\n\r\nGeorgia Owbridge, owbr0002@flinders.edu.au\r\nAdarshkumar Kirankumar Parekh, pare0046@flinders.edu.au\r\nMatilda Lindquist, lind0235@flinders.edu.au\r\nYoussef Ibrahim, ibra0103@flinders.edu.au\r\nJack Pantelios, pant0073@flinders.edu.au',
      long_description_content_type='text/markdown',
      author='Georgia Owbridge',
      author_email='owbr0002@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012022S2LDO1/', package='docassemble.LLAW33012022S2LDO1'),
     )

