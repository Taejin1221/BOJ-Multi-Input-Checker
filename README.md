# BOJ Multi Input Checker
주어진 여러 입력들을 모두 채점해주는 프로그램

- 지원 언어: C++

## 사용법
1. 실행할 파일이 있는 디렉터리
    1. 코드 작성 후 `./a.out`으로 컴파일
    2. `inputs` 파일에 `!@#`을 구분자로하여 예제 입력
        - 예) `inputs`
            ```
            1 2 3
            4 5 6
            !@#
            7 8 9
            10 11 12   
            ```
    3. `outputs` 파일에 `!@#`을 구분자로하여 예제 입력
        - 예) `outputs`
            ```
            3
            !@#
            9
            ```
2. `input_checker.py`가 있는 디렉터리
    1. `settings.json` 파일에 `directory` 정보 입력
        - 파일 작성 예) 
            ```
            {
                "directory": "/Users/UserName/GitHub/ProblemSolving/Baekjoon"
            }
            ```
    2. `input_chcker.py` 실행
        - 결과 예)
            ```
            ===== 테스트 0 =====
            입력
            1 2 3
            4 5 6
            기댓값
            3
            출력
            2
            결과: 틀렸습니다!!
            ===== 테스트 1 =====
            입력
            7 8 9
            10 11 12
            기댓값
            9
            출력
            9
            결과: 맞았습니다!!
            ===== 최종 결과 =====
            정답: 1, 오답: 1
            정답률: 50.00%
            ```
