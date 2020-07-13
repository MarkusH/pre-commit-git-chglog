import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pre-commit-git-chglog",
    author="Markus Holtermann",
    author_email="info@markusholtermann.eu",
    description="Check for git-chglog compatible commit messages",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarkusH/pre-commit-git-chglog",
    packages=setuptools.find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"],
    ),
    install_requires=["PyYAML~=5.3.0"],
    setup_requires=["setuptools_scm>=3.4.2,<4"],
    use_scm_version=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Version Control :: Git",
    ],
    python_requires=">=3.7",
    entry_points={"console_scripts": ["pre-commit-git-chglog = git_chglog:main"]},
)
