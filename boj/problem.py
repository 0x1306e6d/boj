import datetime
import os
import re
import sys
import time

from pathlib import Path
from typing import List

import requests

from bs4 import BeautifulSoup
from bs4.element import Tag
from halo import Halo

from boj import selector
from boj.language import C, CPP, PYTHON


class Sample:
    def __init__(self,
                 sample_number: int,
                 sample_input: List[str],
                 sample_output: List[str]):
        self.number = sample_number
        self.input = sample_input
        self.output = sample_output


class Problem:
    def __init__(self,
                 language: str,
                 number: int,
                 title: str,
                 url: str,
                 time_limit: str,
                 memory_limit: str,
                 samples: List[Sample]):
        self.language = language
        self.number = number
        self.title = title
        self.url = url
        self.time_limit = time_limit
        self.memory_limit = memory_limit
        self.samples = samples

    def _comment_begin(self) -> str:
        """
        :returns: 언어의 문법에 맞는 주석 시작.
        """
        raise NotImplementedError()

    def _comment_end(self) -> str:
        """
        :returns: 언어의 문법에 맞는 주석 끝.
        """
        raise NotImplementedError()

    def _whitespace(self) -> str:
        """
        :returns: 언어의 화이트스페이스.
        """
        raise NotImplementedError()

    def write(self) -> None:
        """
        문제를 파일에 쓴다.
        파일 이름은 {문제 번호}.{언어} 이다.
        """
        filename = '{}.{}'.format(self.number, self.language)
        text = "{} 언어로 문제 {} ({}) 를(을) 파일 {} 에 쓰는 중...".format(
            self.language, self.number, self.title, filename
        )
        with Halo(text=text, spinner='dots') as halo:
            # TODO(@ghkim3221): 순환 참조. 파일에 쓰는 부분을 외부 모듈로 옮겨야 함.
            from boj.header import make_header
            header = make_header(self)

            path_to_write = Path(filename)
            if path_to_write.exists():
                halo.fail("이미 파일 {} 이 존재합니다.".format(filename))
                return

            with open(filename, mode='w', encoding='utf8', newline='') as f:
                for header_item in header:
                    f.write(header_item)

            halo.succeed(
                "{} 언어로 문제 {} ({}) 를(을) 파일 {} 에 생성하였습니다.".format(
                    self.language, self.number, self.title, filename
                )
            )


class CProblem(Problem):
    def __init__(self,
                 number: int,
                 title: str,
                 url: str,
                 time_limit: str,
                 memory_limit: str,
                 samples: List[Sample]):
        super(CProblem, self).__init__(C,
                                       number,
                                       title,
                                       url,
                                       time_limit,
                                       memory_limit,
                                       samples)

    def _comment_begin(self) -> str:
        return '/*'

    def _comment_end(self) -> str:
        return '*/'

    def _whitespace(self) -> str:
        return '\t'


class CppProblem(Problem):
    def __init__(self,
                 number: int,
                 title: str,
                 url: str,
                 time_limit: str,
                 memory_limit: str,
                 samples: List[Sample]):
        super(CppProblem, self).__init__(CPP,
                                         number,
                                         title,
                                         url,
                                         time_limit,
                                         memory_limit,
                                         samples)

    def _comment_begin(self) -> str:
        return '/*'

    def _comment_end(self) -> str:
        return '*/'

    def _whitespace(self) -> str:
        return '\t'


class PythonProblem(Problem):
    def __init__(self,
                 number: int,
                 title: str,
                 url: str,
                 time_limit: str,
                 memory_limit: str,
                 samples: List[Sample]):
        super(PythonProblem, self).__init__(PYTHON,
                                            number,
                                            title,
                                            url,
                                            time_limit,
                                            memory_limit,
                                            samples)

    def _comment_begin(self) -> str:
        return '"""'

    def _comment_end(self) -> str:
        return '"""'

    def _whitespace(self) -> str:
        return '    '


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


def _make_url(number: int) -> str:
    return 'https://www.acmicpc.net/problem/{}'.format(number)


def _parse_title(soup: BeautifulSoup) -> str:
    title_tag = soup.select_one(selector.title())
    if title_tag is None:
        return None

    raw_title = title_tag.string
    if raw_title is None:
        return None

    title = raw_title.strip()
    return title


def _parse_time_limit(soup: BeautifulSoup) -> str:
    time_limit_tag = soup.select_one(selector.time_limit())
    if time_limit_tag is None:
        return None

    raw_time_limit = time_limit_tag.string
    if raw_time_limit is None:
        return None

    time_limit = raw_time_limit.strip()
    return time_limit


def _parse_memory_limit(soup: BeautifulSoup) -> str:
    memory_limit_tag = soup.select_one(selector.memory_limit())
    if memory_limit_tag is None:
        return None

    raw_memory_limit = memory_limit_tag.string
    if raw_memory_limit is None:
        return None

    memory_limit = raw_memory_limit.strip()
    return memory_limit


def _parse_sample_tag(sample_tag: Tag) -> List[str]:
    if sample_tag is None:
        return []

    raw = sample_tag.string
    if raw is None:
        return []

    linesep_splitted = re.split('{\r|\n|\r\n|\n\r}', raw)
    empty_filtered = list(filter(lambda s: s != '', linesep_splitted))
    return empty_filtered


def _parse_sample(number: int,
                  sample_input_tag: Tag,
                  sample_output_tag: Tag) -> Sample:
    sample_input = _parse_sample_tag(sample_input_tag)
    sample_output = _parse_sample_tag(sample_output_tag)
    return Sample(number, sample_input, sample_output)


def _parse_samples(soup: BeautifulSoup) -> List[Sample]:
    samples = []

    number = 1
    while True:
        sample_input_selector = selector.sample_input(number)
        sample_input_tag = soup.select_one(sample_input_selector)

        sample_output_selector = selector.sample_output(number)
        sample_output_tag = soup.select_one(sample_output_selector)

        if (sample_input_tag is None) and (sample_output_tag is None):
            break

        sample = _parse_sample(number, sample_input_tag, sample_output_tag)
        samples.append(sample)

        number += 1

    return samples


def _fetch_problem(number: int, language: str) -> Problem:
    with Halo(text="문제 {} 의 데이터를 다운로드 하는 중...".format(number),
              spinner='dots') as halo:
        fetch_start = time.time()

        url = _make_url(number)
        response = requests.get(url)
        if not response.ok:
            if response.status_code == 404:
                halo.fail("문제 {} 는 존재하지 않습니다.".format(number))
                return None
            else:
                halo.fail("문제 {} 의 데이터를 다운로드할 수 없습니다.".format(number))
                raise Exception()

        fetch_end = time.time()
        fetch_duration = (fetch_end - fetch_start)
        halo.succeed(
            "문제 {} 의 데이터를 다운로드 하였습니다. ({:.2f} 초 사용됨, {})".format(
                number, fetch_duration, url
            )
        )

        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        title = _parse_title(soup)
        time_limit = _parse_time_limit(soup)
        memory_limit = _parse_memory_limit(soup)
        samples = _parse_samples(soup)

        problem_class = None
        if language == C:
            problem_class = CProblem
        elif language == CPP:
            problem_class = CppProblem
        elif language == PYTHON:
            problem_class = PythonProblem

        if problem_class is None:
            raise Exception()
        return problem_class(number,
                             title,
                             url,
                             time_limit,
                             memory_limit,
                             samples)


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

    return _fetch_problem(number, language)
