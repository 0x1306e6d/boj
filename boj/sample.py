from bs4.element import Tag


class Sample:
    def __init__(self,
                 sample_number: int,
                 sample_input: str,
                 sample_output: str):
        self.number = sample_number
        self.input = sample_input
        self.output = sample_output


def _parse_sample_tag(sample_tag: Tag) -> str:
    if sample_tag is None:
        return None

    raw_sample = sample_tag.string
    if raw_sample is None:
        return None

    sample = raw_sample.rstrip()
    return sample


def parse_sample(number: int,
                 sample_input_tag: Tag,
                 sample_output_tag: Tag) -> Sample:
    """
    예제 입력 및 출력을 파싱하여 예제 객체를 생성한다.

    :param number: 예제 번호.
    :param sample_input_tag: BeautifulSoup4로 파싱한 예제 번호에 해당하는 입력 태그.
    :param sample_output_tag: BeautifulSoup4로 파싱한 예제 번호에 해당하는 출력 태그.

    :returns: 예제 객체.
    """
    sample_input = _parse_sample_tag(sample_input_tag)
    sample_output = _parse_sample_tag(sample_output_tag)
    return Sample(number, sample_input, sample_output)
