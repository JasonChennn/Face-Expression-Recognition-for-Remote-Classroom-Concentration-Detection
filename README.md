# 即時臉部表情辨識應用於遠距上課專心程度檢測
&emsp;&emsp;以臉部影像辨識運算作為基底，並根據即時的表情來進行推論；場景會假設一位學生正在課堂上，凝視螢幕或者顯示器的表情，基於CNN的深層網路架構進行臉部辨識，來推論短時間內的連續表情影像中，所得到的專心程度分數；該項目旨在利用深度卷積神經網絡，將一個人臉上的情緒應用在專心程度的模擬環境上，該模型是在國際機器學習會議ICML上發表的FER-2013資料集。
## 模型架構
![](https://i.imgur.com/vKE6NIA.png)
&emsp;&emsp;如上圖為我自製的模型示意圖，為了能在邊緣運算裝置上暢行的推論，共採用了4層的CNN架構，因此，在架構與準確度上採取了一個平衡；其中，在每2層的架構中都有採用Dropout來避免過擬和，而Activity Function採用ReLU，則可以在擴展層數的增加前提下，可以防止梯度消失。
## 如何訓練
1. 我並沒有提供已訓練好的模型權重，所以你必須先下載Fer2013的資料集。(連結在下面附錄)
2. 設定Epoch回合, Batch Size大小, Validation Set張數。
3. 執行main.py裡的Train。
4. 系統產生model.h5檔，訓練完成。
## 如何即時推論
1. 執行main.py裡的Inference。
2. 利用**Haar Feature-Based Cascade**方法來檢測網絡攝像頭畫面中的每個幀人臉。
3. 包含人臉的圖像區域被降解析度為**48x48**，並作為輸入。
4. 臉部情緒專心程度的表情顯示在影像上。
5. 推論結束，顯示專心與分心的狀態。
### 專心程度評分標準
* 專心(Concentrate Score): 最高加5分代表最專心，其次3分，最低1分。
* 分心(Absent Score): 最高扣5分代表最分心，其次3分，最低1分。
### 實驗結果
下圖為僅有FER2013資料集以及訓練Epoch為50回的結果：
![](https://i.imgur.com/yi7mxYh.png)
## 結論
&emsp;&emsp;我們這次是基於邊緣運算的模擬上，來建構深層網路，因此在準確率以及硬體負載取得一個平衡，可以為線上遠距教學平台提供，教師與學生們之間的雙向互動檢測方式，我相信這是有意義的，因為諸多學生不是每個人都可以負荷高硬體成本的價格，因此若可以將該應用以邊緣運算的成本普及，相信在教育上或遠距教學平台上，可以獲得良好的反饋。
![](https://i.imgur.com/6It3TDq.png)
### 即時檢測結果(「專心」): 
&emsp;常態性上課情緒是較為嚴肅的，排除老師課堂上講笑話且機率是較小的。
### 即時檢測結果(「分心」): 
&emsp;常理來說，正常上課是不會有笑容的，除非是觀看娛樂影片或者與同學的嬉鬧。
### 最終結果圓餅圖
![](https://i.imgur.com/ZLU6e3y.png)
&emsp;&emsp;系統根據分數最後進行機率比值計算，取得專心與分心百分比次數，判斷最終結果。
## 參考文獻
D Erhan, PL Carrier, A Courville, M Mirza, B Hamner, W Cukierski, Y Tang, DH Lee, Y Zhou, C Ramaiah, F Feng, R Li, X Wang, D Athanasakis, J Shawe-Taylor, M Milakov, J Park, R Ionescu, M Popescu, C Grozea, J Bergstra, J Xie, L Romaszko, B Xu, Z Chuang, and Y. Bengio. arXiv 2013.
## 附錄
## 函式庫需求：
* Python 3, [OpenCV](https://opencv.org/), [Tensorflow](https://www.tensorflow.org/)
### 資料集
&emsp;&emsp;[[1] FER2013 dataset in Kaggle](https://www.kaggle.com/deadskull7/fer2013)
