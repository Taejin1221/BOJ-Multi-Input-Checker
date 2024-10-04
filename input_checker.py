import subprocess

with open("inputs", "r") as f:
    inputs = f.read()

with open("outputs", "r") as f:
    outputs = f.read()

for idx, (inp, out) in enumerate(zip(inputs.split("!@#"), outputs.split("!@#"))):
    inp_strip = inp.strip()
    out_strip = out.strip()
    # 두 줄 이상의 문장을 출력하기 위해 repr 사용
    res = subprocess.run("./a.out", input=inp, stdout=subprocess.PIPE, text=True)
    res_strip = res.stdout.strip()

    print(f"#{idx}: ", end='')
    if res_strip == out_strip:
        print("맞았습니다!!")
    else:
        print("틀렸습니다!!")
        print("입력")
        print(inp_strip)
        print("출력")
        print(res_strip)
        print("답")
        print(out_strip)