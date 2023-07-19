---
title: 人工智慧與邊緣運算實務期末專題
---
姓名：陳思杰
學號：M10915047
報告日期：110/06/23 (三)
## 1 作品名稱
&emsp;即時臉部表情辨識應用於遠距上課專心程度檢測
## 2 摘要說明
&emsp;&emsp;透過鏡頭取得人臉影像後，以臉部影像辨識運算作為基底，並根據表情來進行推論；場景會假設一位學生正在課堂上，凝視螢幕或者顯示器的表情，基於CNN的深層網路架構進行臉部辨識，來推論短時間內的連續表情影像中，所得到的專心程度分數。
## 3 系統簡介
### 3.1 創作發想
&emsp;&emsp;該項目旨在利用深度卷積神經網絡，將一個人臉上的情緒應用在專心程度的模擬環境上，該模型是在國際機器學習會議ICML上發表的FER-2013數據集以及本專題的額外新增的資料集上訓練，共超過35887張以48x48大小的人臉圖像組成。
### 3.2 硬體架構
* OS: Windows 10
* CPU: Intel I5-10400
* GPU: MSI GTX 1660-Super Gaming
* RAM: DDR4 16G-2333
### 3.3 工作原理及流程
#### 訓練
1.首先載入人臉影像資料集並將其放入對應的標籤資料夾裡。
2.設定Epoch回合, Batch Size大小, Validation Set張數。
3.啟動源碼資料夾中的train.cmd進行訓練。
4.系統產生model.h5檔，訓練完成。
#### 推論
1. 首先，執行display.cmd來進行推論
2. 原理為使用**Haar Feature-Based Cascade**方法來檢測網絡攝像頭畫面中的每個幀人臉。
3. 包含人臉的圖像區域被調整為**48x48**，並被**ReLu**作為輸入。
4. 該網絡為情緒輸出一個**Softmax**層。
5. 臉部情緒專心程度的分數被顯示在即時影像上。
6. 將專心程度評分統計至圖表上。
7. 透過評分顯示上課專心的結果，推論結束。
#### 專心程度評分標準
* 專心(Concentrate Score): 最高加5分代表最專心，其次3分，最低1分。
* 分心(Absent Score): 最高扣5分代表最分心，其次3分，最低1分。
* 圓餅圖計算方式: 
    * 專心程度(Score) = Concentrate / Concentrate + Absent
    * 分心程度(Score) = Absent / Concentrate + Absent
### 3.4 資料集建立方式
&emsp;&emsp;以csv類型的檔案提供，不過我已經轉換為PNG or Jpg格式的圖像數據集，來用於訓練以及測試；如果你想訓練新的數據集，並且做影像大小的前處理，可參考我個人撰寫的alignment.py，來對人臉進行校正以及統一大小；
### 3.5 模型選用與訓練
#### 關於模型架構
![](https://i.imgur.com/vKE6NIA.png)
&emsp;&emsp;如上圖為我自製的模型示意圖，共採用了四層的CNN架構，之所以採用的層數不高，是為了能在邊緣運算裝置上暢行的推論，因此我在架構與準確度上採取了一個平衡；其中，在每兩層的架構中都有採用Dropout來避免過擬和，而Activity Function採用ReLU，則可以在擴展層數的增加前提下，可以防止梯度消失。
#### 關於訓練
&emsp;&emsp;訓練的資料集共分為兩個部分，首先是Training Set，我共準備了29690張來進行訓練；再者，關於Testing Set，我則準備了8187張等八個label值來為專心程度評分。在源碼中，我為各位同學提供了train.cmd，只要將數據及放入源碼資料夾的data中，即可進行訓練；另外，我個人也推薦訓練時可以安裝Nvidia Cuda來進行GPU加速。
#### 詳細參數
* Training Set = 29690張影像，共八個label
* Testing Set = 8187張影像，共八個label
* Batch Size = 64張影像為一組
* Epoch = 100回
## 4 實驗結果
### 4.1 測試與比較
下圖為僅有FER2013資料集以及訓練Epoch為50回的結果：
![](https://i.imgur.com/yi7mxYh.png)

---
下圖為我額外增加三千張的人臉情緒資料集及訓練Epoch為100回的結果：
![](https://i.imgur.com/mzXDyzv.png)
#### 比較兩張結果：
&emsp;&emsp;我們可以發現，經過額外的資料集與較長的Epoch數，在Training Set準確度從上圖的85%提升至94%，而在過程中也成指數型曲線成長；顯而易見的是，失誤也隨之降低。不過較為可惜的是，在Testing Set的失誤不減反增，這的確有待探討。
### 4.2 改進與優化
#### &emsp;&emsp;下圖為進行訓練過程示意圖，從中可以發現，在Epoch第92回時，在訓練時的準確度已經趨近94%，此處在我個人的電腦上(請參考我的硬體規格)跑已經花費了約5小時：
![](https://i.imgur.com/23TC6io.png)

---
## 5 結論
&emsp;&emsp;我們這次是基於邊緣運算的模擬上，來建構深層網路，因此在準確率以及硬體負載取得一個平衡，可以為線上遠距教學平台提供，教師與學生們之間的雙向互動檢測方式，我相信這是有意義的，因為諸多學生不是每個人都可以負荷高硬體成本的價格，因此若可以將該應用以邊緣運算的成本普及，相信在教育上或遠距教學平台上，可以獲得良好的反饋。


---

![](https://i.imgur.com/6It3TDq.png)


---

#### 即時檢測結果(+5分): 「是專心的」
&emsp;(常態性上課情緒是較為嚴肅的，排除老師課堂上講笑話且機率是較小的。)


---

#### 即時檢測結果(-5分): 「是分心的」
&emsp;(常理來說，正常上課是不會有笑容的，除非是觀看娛樂影片或者與同學的嬉鬧。)

#### 最終結果圓餅圖
![](https://i.imgur.com/ZLU6e3y.png)
&emsp;&emsp;系統根據分數最後進行機率比值計算，取得專心與分心百分比次數，判斷最終結果。

## 6 參考文獻
D Erhan, PL Carrier, A Courville, M Mirza, B Hamner, W Cukierski, Y Tang, DH Lee, Y Zhou, C Ramaiah, F Feng, R Li, X Wang, D Athanasakis, J Shawe-Taylor, M Milakov, J Park, R Ionescu, M Popescu, C Grozea, J Bergstra, J Xie, L Romaszko, B Xu, Z Chuang, and Y. Bengio. arXiv 2013.
## 7 附錄
### 7.1 Python源碼
#### 編譯器與函式庫需求：
* Python 3, [OpenCV](https://opencv.org/), [Tensorflow](https://www.tensorflow.org/)
* To install the required packages, run `pip install -r requirements.txt`.
#### 檔案說明：
* emotions(.py): 主程式，包含訓練資料及以及即時影像推論
* alignment(.py): 人臉影像批次前處理，包含調整影像大小，人臉位置校正
* rename_batch(.py): 批次重新命名，以便新增資料集使用
* haarcascade_frontalface_default(.xml): 人臉特徵分類器
* model(.h5): 我已訓練好的Model，為100回Epoch
* train(.cmd): Windows OS指令集，進行訓練用
* display(.cmd): Windows OS指令集，進行推論用

#### 下載連結：
https://github.com/M10915047/Face-Expression-Recognition-for-Remote-Classroom-Concentration-Detection

### 7.2 資料集及標註檔
&emsp;&emsp;[[1] FER2013 dataset in Kaggle](https://www.kaggle.com/deadskull7/fer2013)
&emsp;&emsp;[[2] 本人額外預處裡之資料集約三千張](https://drive.google.com/drive/folders/1Du7r1XYwi_d5mhFtFyHk5B-Z9PMjymOB?usp=sharing)

### 附錄一: 推論(Colab版本)
[Github下載連結](https://github.com/M10915047/Face-Expression-Recognition-for-Remote-Classroom-Concentration-Detection/tree/main/InferForColab)

* 說明:我在Github準備了一個資料夾，專門提供給讀者可以在Colab上面執行，裡面共含了4個檔案，分別為：
    1. inference.ipynb: 主程式源碼
    2. haarcascade_frontalface_default.xml: 人臉分類器
    3. model.h5: 已訓練好的模型
    4. demo.mp4: 我個人提供的人臉短片提供推論
    
P.S. 請務必將上述檔案上傳至Colab的tmp資料夾裡面，或亦可自行修改源碼更改路徑。


---

以下為演繹圖:
![](https://i.imgur.com/PsgzgXa.png)
