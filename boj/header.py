import datetime
import os

from boj.problem import Problem, Sample


__DATETIME_FORMAT__ = "%Y-%m-%d %H:%M:%S"


def _make_file_header(problem: Problem) -> str:
    return '{}File: {}.{}'.format(problem._whitespace(),
                                  problem.number,
                                  problem.language)


def _make_title_header(problem: Problem) -> str:
    return '{}Title: {}'.format(problem._whitespace(), problem.title)


def _make_url_header(problem: Problem) -> str:
    return '{}URL: {}'.format(problem._whitespace(), problem.url)


def _make_sample_header(problem: Problem, sample: Sample) -> str:
    input_header = '{}Input #{}:{}'.format(problem._whitespace(),
                                           sample.number,
                                           os.linesep)
    input_header_content = os.linesep.join(
        ['{}{}{}'.format(problem._whitespace(),
                         problem._whitespace(),
                         sample_input) for sample_input in sample.input]
    )
    output_header = '{}Output #{}:{}'.format(problem._whitespace(),
                                             sample.number,
                                             os.linesep)
    output_header_content = os.linesep.join(
        ['{}{}{}'.format(problem._whitespace(),
                         problem._whitespace(),
                         sample_output) for sample_output in sample.output]
    )

    return '{}{}{}{}{}'.format(input_header,
                               input_header_content,
                               os.linesep,
                               output_header,
                               output_header_content)


def _make_samples_header(problem: Problem) -> str:
    sample_headers = []

    for sample in problem.samples:
        sample_header = _make_sample_header(problem, sample)
        sample_headers.append(sample_header)

    return os.linesep.join(sample_headers)


def _make_created_at_header(problem: Problem) -> str:
    now = datetime.datetime.now()
    return '{}Created At: {}'.format(problem._whitespace(),
                                     now.strftime(__DATETIME_FORMAT__))


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
    created_at_header = _make_created_at_header(problem)

    return os.linesep.join([
        problem._comment_begin(),
        file_header,
        title_header,
        url_header,
        samples_header,
        created_at_header,
        problem._comment_end()
    ])
