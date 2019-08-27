from setuptools import setup

setup(
    name="boj",
    version="0.0.1",
    url="https://github.com/ghkim3221/boj",
    author="Gihwan Kim",
    author_email="ghkim3221@gmail.com",
    license="MIT",
    description="깔끔한 Baekjoon Online Judge 코드 관리를 위한 커맨드 라인 명령어",
    install_requires=[
        'fire'
    ],
    packages=[
        'boj'
    ],
    entry_points={
        'console_scripts': [
            'boj = boj.main:main'
        ]
    },
)
