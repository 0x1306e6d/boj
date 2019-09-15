import os
import sys

from fire import Fire

from boj.problem import create_problem


def new(number: str, language: str) -> None:
    """
    새로운 문제를 생성한다.

    :param number: 문제 번호.
    :param language: 언어.
    """

    try:
        number = int(number)
    except ValueError:
        sys.stderr.write(
            "잘못된 문제 번호 {} 를(을) 입력하였습니다.".format(number)
        )
        sys.stderr.write(os.linesep)
        sys.exit(1)

    problem = create_problem(number, language)
    problem.write()
    print(
        "{} 언어로 문제 {} ({}) 를(을) 생성하였습니다.".format(
            problem.language, problem.number, problem.title,
        )
    )


def main() -> None:
    Fire({
        'new': new,
    })
