# boj

깔끔한 Baekjoon Online Judge 코드 관리를 위한 커맨드 라인 명령어

## Getting Started

### Installation

아직 설치를 제공하지 않습니다. 이 프로젝트를 클론하신 후 `python setup.py install` 명령으로 설치해주세요.

### Usage

 - `boj new {문제번호} {언어}`
   - `{문제번호}`에 해당하는 문제의 정보를 읽어 문제 파일을 생성합니다.
   - `{언어}`는 C, C++, Python을 지원합니다.
     - C: `c`
     - C++: `c++`, `cpp`
     - Python: `python`, `py`
     - Java: `java`
   - Examples:
     ```
     $ boj new 1000 cpp
     ✔ 문제 1000 의 데이터를 다운로드 하였습니다. (0.39 초 사용됨, https://www.acmicpc.net/problem/1000)
     ✔ cpp 언어로 문제 1000 (A+B) 를(을) 파일 1000.cpp 에 생성하였습니다.
     ```

## License

```
MIT License

Copyright (c) 2019 - 2020 Gihwan Kim

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
