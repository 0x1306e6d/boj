import datetime
import os

from boj.problem import Problem
from boj.sample import Sample


def _make_file_header(problem: Problem) -> str:
    return 'File: {}.{}'.format(problem.number, problem.language)


def _make_title_header(problem: Problem) -> str:
    return 'Title: {}'.format(problem.title)


def _make_url_header(problem: Problem) -> str:
    return 'URL: {}'.format(problem.url)


def _make_sample_header(sample: Sample) -> str:
    input_header = 'Input #{}:{}{}'.format(sample.number,
                                           os.linesep,
                                           sample.input)
    output_header = 'Output #{}:{}{}'.format(sample.number,
                                             os.linesep,
                                             sample.output)

    return '{}{}{}'.format(input_header, os.linesep, output_header)


def _make_samples_header(problem: Problem) -> str:
    sample_headers = []

    for sample in problem.samples:
        sample_header = _make_sample_header(sample)
        sample_headers.append(sample_header)

    return os.linesep.join(sample_headers)


def _make_created_at_header() -> str:
    return 'Created At: {}'.format(datetime.datetime.now())


def make_header(problem: Problem) -> str:
    """
    문제의 헤더 주석을 생성한다.

    :param problem: 문제 객체.

    :returns: 헤더 주석
    """
    file_header = _make_file_header(problem)
    title_header = _make_title_header(problem)
    url_header = _make_url_header(problem)
    samples_header = _make_samples_header(problem)
    created_at_header = _make_created_at_header()

    return os.linesep.join([
        problem._comment_begin(),
        file_header,
        title_header,
        url_header,
        samples_header,
        created_at_header,
        problem._comment_end()
    ])
