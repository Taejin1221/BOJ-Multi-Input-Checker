import json
import os
import subprocess

with open("settings.json", "r") as f:
    settings = json.load(f)
os.chdir(settings["directory"])

with open("inputs", "r") as f:
    inputs = f.read().split("!@#")

with open("outputs", "r") as f:
    outputs = f.read().split("!@#")

accept = 0
for idx, (inp, out) in enumerate(zip(inputs, outputs)):
    inp, out = inp.strip(), out.strip()

    res = subprocess.run("./a.out", input=inp, stdout=subprocess.PIPE, text=True)
    res = res.stdout.strip()

    print(f"===== 테스트 {idx} =====")
    print("입력")
    print(inp)
    print("기댓값")
    print(out)
    print("출력")
    print(res)

    print("결과: ", end='')
    if res == out:
        accept += 1
        print("맞았습니다!!")
    else:
        print("틀렸습니다!!")

print("===== 최종 결과 =====")
input_size = len(inputs)
print(f"정답: {accept}, 오답: {input_size - accept}")
print(f"정답률: {accept / input_size * 100:.2f}%")
