# 楓之谷 M 猜數字

## 使用方式
1. 點擊 `exe` 檔執行
2. 每一輪按 `y` 開始，按 `n` 退出
3. 電腦會告訴你他猜的數字，你就照打到遊戲
4. 告訴電腦幾 `A` 幾 `B` (就是 `O` 和 `△`)，`X` 就都 0
5. 電腦會告訴你剩餘答案庫和下一個數字
6. 最後猜到記得給 `3A0B`

## 檔案說明
* guess_num.py：玩家提供幾 A 幾 B，由電腦根據線索猜測
* guess_num_test.py：讓電腦自己玩，紀錄平均使用局數與平均第一輪的答案庫大小

## python 轉 exe
使用 `pyinstaller` 會需要 `hidden-import`
```
pyinstaller -F guess_num.py --hidden-import=numpy.random.common --hidden-import=numpy.random.bounded_integers --hidden-import=numpy.random.entropy
```
