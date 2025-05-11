import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x = sp.Symbol('x')

def is_valid_function(expr_str):
    try:
        expr = sp.sympify(expr_str)
        expr.subs(x, 1)  # x에 1 대입해서 오류 체크
        return True
    except (sp.SympifyError, TypeError, ValueError):
        return False

def plot_function(expr_str):
    expr = sp.sympify(expr_str)
    func = sp.lambdify(x, expr, modules=['numpy'])

    x_vals = np.linspace(-10, 10, 1000)
    try:
        y_vals = func(x_vals)
    except Exception as e:
        print(f"그래프를 그릴 수 없습니다: {e}")
        return

    plt.figure(figsize=(8, 5))
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.plot(x_vals, y_vals, label=f"y = {expr_str}")
    plt.legend()
    plt.title("함수 그래프")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def main():
    print("함수 입력 예시:")
    print("- 다항함수: x**2 + 3*x + 2")
    print("- 지수함수: exp(x) 또는 2**x")
    print("- 로그함수: log(x) 또는 log(x, 2)")
    print("- 삼각함수: sin(x), cos(x), tan(x)\n")

    while True:
        user_input = input("함수를 입력하세요 (예: x**2 + 2*x + 1): ")
        if is_valid_function(user_input):
            try:
                plot_function(user_input)
                break
            except Exception as e:
                print(f"그래프 오류: {e}")
        else:
            print("함수가 아닙니다. 다시 입력해주세요.\n")

if __name__ == "__main__":
    main()
