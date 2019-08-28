import os
import sys

import bs4
import requests

from boj import selector
from boj.language import C, CPP, PYTHON


class Problem:
    def __init__(self, number: int, language: str):
        self.number = number
        self.language = language
        self.url = 'https://www.acmicpc.net/problem/{}'.format(number)
        self.title = None
        self.time_limit = None
        self.memory_limit = None
        self.samples = []

    def _fetch(self) -> None:
        """
        Baekjoon Online Judge 웹사이트의 문제 번호에 해당하는 문제의 데이터를 
        가져온다. 가져오는 데이터의 종류는 다음과 같다.

        * 문제 이름
        * 시간 제한
        * 메모리 제한
        * 예제 입력
        * 예제 출력
        """
        response = requests.get(self.url)
        if not response.ok:
            raise Exception()

        html = response.text
        soup = bs4.BeautifulSoup(html, 'html.parser')

        self.title = soup.select_one(selector.title()).string
        self.time_limit = soup.select_one(selector.time_limit()).string
        self.memory_limit = soup.select_one(selector.memory_limit()).string

        sample_number = 1
        while True:
            sample_input_selector = selector.sample_input(sample_number)
            sample_output_selector = selector.sample_output(sample_number)

            sample_input = soup.select_one(sample_input_selector)
            sample_output = soup.select_one(sample_output_selector)

            if (sample_input is None) and(sample_output is None):
                break
            else:
                sample_input = sample_input.string
                sample_output = sample_output.string
                self.samples.append((sample_input, sample_output))

                sample_number += 1

    def write(self) -> None:
        """
        문제를 파일에 쓴다.
        파일 이름은 {문제 번호}.{언어} 이다.
        """
        self._fetch()

        filename = '{}.{}'.format(self.number, self.language)
        f = open(filename, mode='w', encoding='utf8')
        f.close()


class CProblem(Problem):
    def __init__(self, number: int):
        super(CProblem, self).__init__(number, C)


class CppProblem(Problem):
    def __init__(self, number: int):
        super(CppProblem, self).__init__(number, CPP)


class PythonProblem(Problem):
    def __init__(self, number: int):
        super(PythonProblem, self).__init__(number, PYTHON)


def parse_language(language: str) -> str:
    """
    language를 파싱한다.
    한 언어에 대해 여러 입력이 들어올 수 있으므로, 이들을 하나로 일반화 한다.

    :param language: 언어.

    :returns: 일반화된 언어. 이는 해당 언어의 파일 확장자와 같다.
    """

    if language == 'c':
        return C
    elif (language == 'cpp') or (language == 'c++'):
        return CPP
    elif (language == 'python') or (language == 'py'):
        return PYTHON


def create_problem(number: int, raw_language: str) -> Problem:
    """
    language에 해당하는 문제 객체를 생성한다.

    :param number: 문제 번호.
    :param language: 언어.

    :returns: 문제 객체.
    """

    language = parse_language(raw_language)
    if language is None:
        sys.stderr.write(
            "지원하지 않는 언어 {} 를(을) 입력하였습니다.".format(raw_language)
        )
        sys.stderr.write(os.linesep)
        sys.exit(1)

    if language == C:
        return CProblem(number)
    elif language == CPP:
        return CppProblem(number)
    elif language == PYTHON:
        return PythonProblem(number)
