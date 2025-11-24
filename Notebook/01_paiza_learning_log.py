# %%
import traceback
import sys
# %%
# 例外処理
## 簡単な例外処理

print(1)
try:
    number = 0
    answer = 100 / number
    print(answer)
except ZeroDivisionError:
    print("0では割り算できません")
    # print(traceback.format_exc())
    sys.stderr.write(traceback.format_exc())
finally:
    print(2)
# %%
print(1)
try:
    number = 0
    answer = 100 / number
    print(answer)
except ZeroDivisionError as e:
    print("0では割り算できません")
    print(e)
except NameError as e:
    print("未定義の変数を呼び出しています")
    print(e)
except Exception:
    print("予期せぬエラーが発生しました")
finally:
    print(2)
# %%
