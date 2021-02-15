import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="digitalbits-core-prometheus-exporter",
    version="0.9.7",
    author="DigitalBits Development Foundation",
    author_email="ops@digitalbits.org",
    description="Export digitalbits core metrics in prometheus format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/digitalbits/digitalbits-core-prometheus-exporter",
    include_package_data=True,
    keywords=["prometheus", "exporter", "digitalbits"],
    license="Apache Software License 2.0",
    entry_points={
        'console_scripts': [
            'digitalbits-core-prometheus-exporter=digitalbits_core_prometheus_exporter:run',
        ],
    },
    packages=setuptools.find_packages(),
    install_requires=["prometheus_client", "requests"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Information Technology",
        "Topic :: System :: Monitoring",
        "License :: OSI Approved :: Apache Software License",
    ],
)
