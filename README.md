# EEating

Welcome to EEating.

Eat to live, not live to eat.

## Usage

```
usage: bash run.sh ${port}
```

### Prerequisites

```
pip3 install django
```

## demo(in NTU)

```
http://163.28.17.76:8000/
```

## func

這是一個關於外送程式的後端應用。管理者可以從localhost:8000/admin去管理database裡的內容。裡面有幾種物件：Product是要賣的東西，ProductInstance是真正要賣的商品(一種product可以有很多個），Seller是關於賣家的資訊，Genre是每件商品的分類。在首頁，可以顯示出每種類別的數量。上面已經完成的連結是Product，點進去可以看到product列出來，再點進去可以看到詳細資訊。
