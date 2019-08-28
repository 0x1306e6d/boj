def title() -> str:
    """
    :returns: Baekjoon Online Judge 웹사이트의 문제 이름 선택자
    """
    return '#problem_title'


def time_limit() -> str:
    """
    :returns: Baekjoon Online Judge 웹사이트의 시간 제한 선택자
    """
    return '#problem-info > tbody > tr > td:nth-child(1)'


def memory_limit() -> str:
    """
    :returns: Baekjoon Online Judge 웹사이트의 메모리 제한 선택자
    """
    return '#problem-info > tbody > tr > td:nth-child(2)'


def sample_input(sample_number: int) -> str:
    """
    :param sample_number: 예제 번호

    :returns: Baekjoon Online Judge 웹사이트의 예제 입력 선택자
    """
    return '#sample-input-{}'.format(sample_number)


def sample_output(sample_number: int) -> str:
    """
    :param sample_number: 예제 번호

    :returns: Baekjoon Online Judge 웹사이트의 예제 입력 선택자
    """
    return '#sample-output-{}'.format(sample_number)
