import json
import os
import subprocess
import sys

with open("settings.json", "r") as f:
    settings = json.load(f)
os.chdir(settings["directory"])

verbose = 0
if len(sys.argv) > 2 and (sys.argv[1] == "-v" or sys.argv[1] == "--verbose"):
    verbose = int(sys.argv[2])

with open("inputs", "r") as f:
    inputs = f.read().split("!@#")

with open("outputs", "r") as f:
    outputs = f.read().split("!@#")

accept = 0
fail_case = []
for idx, (inp, out) in enumerate(zip(inputs, outputs)):
    inp, out = inp.strip(), out.strip()

    res = subprocess.run("./a.out", input=inp, stdout=subprocess.PIPE, text=True)
    res = res.stdout.strip()

    print(f"===== 테스트 {idx} =====")
    if verbose == 1:
        print("입력")
        print(inp, end='\n\n')
        print("기댓값")
        print(out, end='\n\n')
        print("출력")
        print(res, end='\n\n')

    if res == out:
        accept += 1
        print("맞았습니다!!")
    else:
        print("***** 틀렸습니다!! *****")
        fail_case.append(idx)
        if verbose == 1 or verbose == 2:
            print("결과: 기댓값 vs 출력")
            out_split, res_split = out.split('\n'), res.split('\n')
            for out_one, res_one in zip(out_split, res_split):
                if out_one == res_one:
                    print("정답:", end=" ")
                else:
                    print("*오답*:", end=" ")
                print(f"{out_one} vs {res_one}")

            if len(out_split) > len(res_split):
                print("*오답*:", end=" ")
                for out_one in out_split[len(res_split):]:
                    print(f"{out_one} vs ''")
            elif len(out_split) < len(res_split):
                print("*오답*:", end=" ")
                for res_one in res_split[len(out_split):]:
                    print(f"'' vs {res_one}")
    print("")

print("===== 최종 결과 =====")
input_size = len(inputs)
print(f"정답: {accept}, 오답: {input_size - accept}")
print(f"정답률: {accept / input_size * 100:.2f}%")
if input_size != accept:
    print("오답 케이스:", end=" ")
    print(", ".join(list(map(str, fail_case))))
