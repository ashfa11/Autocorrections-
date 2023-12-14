from distutils.core import setup

setup(
    name="autocorrect",
    version="2.6.1",
    python_requires=">=3.6",
    packages=["autocorrect"],
    package_data={"autocorrect": ["data/en.tar.gz"]},
    package_data={"autocorrect": ["data/ta.xml.bz2"]},
    description="Spelling Corrector",
    author="Jonas McCallum, Filip Sondej",
    author_email="filipsondej@protonmail.com",
    url="https://github.com/fsondej/autocorrect",
    license="https://opensource.org/licenses/LGPL-3.0",
    classifiers=(
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Natural Language :: Tamil",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ),
    keywords="autocorrect spelling corrector nlp multilanguage spellcheck",
)