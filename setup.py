import setuptools
import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("LICENSE", "r") as fh:
    license = fh.read()

setuptools.setup(
    name="mcsm-template",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="ZhengXiong Zhao",
    author_email="zhengxiongzhao@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/mcsm-template",
    license=license,
    platforms='any',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
