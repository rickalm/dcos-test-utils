from setuptools import setup

setup(
    name='dcos-test-utils',
    version='0.1',
    description='DC/OS cluster provisioning and orchestration utilities',
    url='https://dcos.io',
    author='Mesosphere, Inc.',
    author_email='help@dcos.io',
    license='apache2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    packages=['dcos_launch', 'dcos_test_utils', 'cloudcleaner'],
    install_requires=[
        'aiodns',
        'aiohttp',
        'aiohttp-debugtoolbar',
        'aiomysql',
        'azure-common',
        'azure-storage',
        'azure-mgmt-network',
        'azure-mgmt-resource',
        'azure-monitor',
        'boto3',
        'botocore',
        'cerberus',
        'docopt',
        'google-api-python-client',
        'jinja2',
        'msrest',
        'msrestazure',
        'oauth2client==3.0.0',
        'pyinstaller==3.2',
        'py',
        'pytest',
        'pyyaml',
        'requests==2.14.1',
        'retrying',
        'slacker'],
    entry_points={
        'console_scripts': [
            'dcos-launch=dcos_launch.cli:main',
        ],
    },
    package_data={
        'cloudcleaner': ['report.html.jinja'],
        'dcos_launch': ['sample_configs/*.yaml'],
        'dcos_test_utils': [
            'ip-detect/aws.sh',
            'ip-detect/aws_public.sh',
            'ip-detect/gce.sh',
            'ip-detect/gce_public.sh',
            'templates/vpc-cluster-template.json',
            'templates/vpc-ebs-only-cluster-template.json'
        ],
    }
)
