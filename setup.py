# setup.py
from setuptools import setup,find_packages

setup(
    # 包名，应与你的包目录名称一致
    name='easyrpa',
    version='0.1.1',
    author='monkeygeek',
    author_email='monkeygeek@qq.com',
    description='easy rpa common tools project',

    # 包的长描述，可以从README.md或长描述文件中读取
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    # 包的URL，通常是你的项目主页或代码仓库地址
    url='https://github.com/monkeyGeek369/EasyRPA-Common',
    license='MIT',

    # 包的分类，从 https://pypi.org/classifiers/ 获取
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    # 包依赖的库，使用要求列表
    install_requires=[
    ],

    # 额外的包或插件依赖
    extras_require={
    },

    # 包含的数据文件，通常是包的数据或资源文件
    package_data={
    },

    # 包含的包，使用find_packages()自动发现所有包和子包
    packages=['easyrpa','easyrpa.enums', 'easyrpa.models', 'easyrpa.tools'],

    # 包中包含的Python脚本
    scripts=[],

    # 包中包含的可执行程序
    entry_points={
    },

    # 包的Python版本要求
    python_requires='>=3.10',

    # 包的关键字
    keywords='EasyRpa, Common, Exception',
)