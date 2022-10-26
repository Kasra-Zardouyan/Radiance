from binance.client import Client
from RadianceIndicatorW import Ui_Form
import sys
import time

from PyQt5 import QtWidgets as QW
from PyQt5 import QtCore as QC

def Merge_Sort(Arr):
    if len(Arr) > 1:
        Mid = len(Arr)//2
        L = Arr[:Mid]
        R = Arr[Mid:]
        Merge_Sort(L)
        Merge_Sort(R)
 
        i = j = k = 0
        while i < len(L) and j < len(R):
            if (L[i][1] > R[j][1] or (L[i][1] == R[j][1] and L[i][2] > R[j][2]) or (L[i][1] == R[j][1] and L[i][2] == R[j][2] and L[i][3] > R[j][3])):
                Arr[k] = L[i]
                i += 1
            else:
                Arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            Arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            Arr[k] = R[j]
            j += 1
            k += 1

client = Client('hNsmOkyoYCxtr3mLsJRZtQh8GFSIZwIO1428Yzua9ePG9Dgq0yAXDZh5NmvwFK6F', 'abjnclzCMbxkomH4i4SX9LdYw1WyqIzHS3ytAI2s5HRYplpgpOjiOACyEhZtp9pD')
TimeStamp = "4H"
Test = ["1INCHUSDT", "AAVEUSDT", "ACMUSDT", "ADAUSDT", "AIONUSDT", "AKROUSDT", "ALGOUSDT", "ALICEUSDT", "ALPHAUSDT", "ANKRUSDT", "ANTUSDT", "ARDRUSDT", "ARPAUSDT", "ASRUSDT", "ATMUSDT", "ATOMUSDT", "AUDIOUSDT", "AUDUSDT", "AVAUSDT", "AVAXUSDT", "AXSUSDT", "BADGERUSDT", "BALUSDT", "BANDUSDT", "BATUSDT", "BCHUSDT", "BEAMUSDT", "BELUSDT", "BLZUSDT", "BNBUSDT", "BNTUSDT", "BTCUSDT", "BTSUSDT", "BTTUSDT", "BUSDUSDT", "BZRXUSDT", "CAKEUSDT", "CELOUSDT", "CELRUSDT", "CHRUSDT", "CHZUSDT", "CKBUSDT", "COCOSUSDT", "COMPUSDT", "COSUSDT", "COTIUSDT", "CRVUSDT", "CTKUSDT", "CTSIUSDT", "CTXCUSDT", "CVCUSDT", "DASHUSDT", "DATAUSDT", "DCRUSDT", "DEGOUSDT", "DENTUSDT", "DGBUSDT", "DIAUSDT", "DNTUSDT", "DOCKUSDT", "DODOUSDT", "DOGEUSDT", "DOTUSDT", "DREPUSDT", "DUSKUSDT", "EGLDUSDT", "ENJUSDT", "EOSUSDT", "ETCUSDT", "ETHUSDT", "EURUSDT", "FETUSDT", "FILUSDT", "FIOUSDT", "FIROUSDT", "FISUSDT", "FLMUSDT", "FTMUSDT", "FTTUSDT", "FUNUSDT", "GBPUSDT", "GRTUSDT", "GTOUSDT", "GXSUSDT", "HARDUSDT", "HBARUSDT", "HIVEUSDT", "HNTUSDT", "HOTUSDT", "ICXUSDT", "INJUSDT", "IOSTUSDT", "IOTAUSDT", "IOTXUSDT", "IRISUSDT", "JSTUSDT", "JUVUSDT", "KAVAUSDT", "KEYUSDT", "KMDUSDT", "KSMUSDT", "KNCUSDT", "LINKUSDT", "LITUSDT", "LRCUSDT", "LSKUSDT", "LTCUSDT", "LTOUSDT", "LUNAUSDT", "MANAUSDT", "MATICUSDT", "MBLUSDT", "MDTUSDT", "MFTUSDT", "MITHUSDT", "MKRUSDT", "MTLUSDT", "NANOUSDT", "NBSUSDT", "NEARUSDT", "NEOUSDT", "NKNUSDT", "NMRUSDT", "NPXSUSDT", "NULSUSDT", "OCEANUSDT", "OGNUSDT", "OGUSDT", "OMGUSDT", "OMUSDT", "ONEUSDT", "ONGUSDT", "ONTUSDT", "ORNUSDT", "OXTUSDT", "PAXGUSDT", "PAXUSDT", "PERLUSDT", "PNTUSDT", "PONDUSDT", "PSGUSDT", "QTUMUSDT", "REEFUSDT", "RENUSDT", "REPUSDT", "RIFUSDT", "RLCUSDT", "ROSEUSDT", "RSRUSDT", "RUNEUSDT", "RVNUSDT", "SANDUSDT", "SCUSDT", "SFPUSDT", "SKLUSDT", "SNXUSDT", "SOLUSDT", "SRMUSDT", "STMXUSDT", "STORJUSDT", "STPTUSDT", "STRAXUSDT", "STXUSDT", "SUNUSDT", "SUSDUSDT", "SUSHIUSDT", "SXPUSDT", "TCTUSDT", "TFUELUSDT", "THETAUSDT", "TOMOUSDT", "TRBUSDT", "TROYUSDT", "TRUUSDT", "TRXUSDT", "TUSDUSDT", "TWTUSDT", "UMAUSDT", "UNFIUSDT", "UNIUSDT", "USDCUSDT", "UTKUSDT", "VETUSDT", "VITEUSDT", "VTHOUSDT", "WANUSDT", "WAVESUSDT", "WINGUSDT", "WINUSDT", "WNXMUSDT", "WRXUSDT", "WTCUSDT", "XEMUSDT", "XLMUSDT", "XMRUSDT", "XRPUSDT", "XTZUSDT", "XVSUSDT", "YFIIUSDT", "YFIUSDT", "ZECUSDT", "ZENUSDT", "ZILUSDT", "ZRXUSDT"]
Test3 = ["AKROUSDT", "WINUSDT"]
Test2 = ["1INCHUSDT", "AAVEUSDT", "ACMUSDT", "ADAUSDT", "AIONUSDT", "AKROUSDT", "ALGOUSDT", "ALICEUSDT", "ALPHAUSDT", "ANKRUSDT", "ANTUSDT",  "ATMUSDT", "ATOMUSDT", "AUDIOUSDT", "AUDUSDT", "AVAUSDT", "AVAXUSDT"]
Data = []
slog1 = " Radiance Indicator App V:0.8.7"
slog2 = " Welcome,"
pos = 1

class Window(QW.QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.radioButton_5m.ts = "5m"
        self.radioButton_5m.toggled.connect(self.Time_Change)
        self.radioButton_15m.ts = "15m"
        self.radioButton_15m.toggled.connect(self.Time_Change)
        self.radioButton_30m.ts = "30m"
        self.radioButton_30m.toggled.connect(self.Time_Change)
        self.radioButton_1H.ts = "1H"
        self.radioButton_1H.toggled.connect(self.Time_Change)
        self.radioButton_2H.ts = "2H"
        self.radioButton_2H.toggled.connect(self.Time_Change)
        self.radioButton_4H.ts = "4H"
        self.radioButton_4H.toggled.connect(self.Time_Change)
        self.radioButton_6H.ts = "6H"
        self.radioButton_6H.toggled.connect(self.Time_Change)
        self.radioButton_12H.ts = "12H"
        self.radioButton_12H.toggled.connect(self.Time_Change)
        self.radioButton_1D.ts = "1D"
        self.radioButton_1D.toggled.connect(self.Time_Change)
        self.radioButton_3D.ts = "3D"
        self.radioButton_3D.toggled.connect(self.Time_Change)
        self.radioButton_1W.ts = "1W"
        self.radioButton_1W.toggled.connect(self.Time_Change)
        self.radioButton_1M.ts = "1M"
        self.radioButton_1M.toggled.connect(self.Time_Change)
        
        self.pushButton_1.clicked.connect(self.Download_Data)
        self.pushButton_2.clicked.connect(self.Distribution)

    def Distribution(self):
        global pos
        pos = 1
        if self.comboBox_1.currentText() == "":
            self.Empty()        
        elif self.comboBox_1.currentText() == "Ichimoku":
            self.Ichimoku()
        elif self.comboBox_1.currentText() == "R Ichimoku":
            self.Reverse_Ichimoku()
        elif self.comboBox_1.currentText() == "Parabolic SAR":
            self.Parabolic_SAR()
        else:
            self.Empty()
        pos = 2
        if self.comboBox_2.currentText() == "":
            self.Empty()   
        elif self.comboBox_2.currentText() == "Ichimoku":
            self.Ichimoku()
        elif self.comboBox_2.currentText() == "R Ichimoku":
            self.Reverse_Ichimoku()
        elif self.comboBox_2.currentText() == "Parabolic SAR":
            self.Parabolic_SAR()
        else:
            self.Empty()   
        pos = 3
        if self.comboBox_3.currentText() == "":
            self.Empty()   
        elif self.comboBox_3.currentText() == "Ichimoku":
            self.Ichimoku()
        elif self.comboBox_3.currentText() == "R Ichimoku":
            self.Reverse_Ichimoku()
        elif self.comboBox_3.currentText() == "Parabolic SAR":
            self.Parabolic_SAR()
        else:
            self.Empty()   

    def Time_Change(self):
        global TimeStamp
        radioButton = self.sender()
        if radioButton.isChecked():
            TimeStamp = radioButton.ts

    def Download_Data(self):
        global slog1, Data, Test
        Data = []
        self.log_2.setText(slog1)
        slog1 = " Downloading data..."
        self.log_1.setText(slog1)
        if (TimeStamp == "5m"):
            for Cur in Test:
                Candles = client.get_historical_klines(Cur, Client.KLINE_INTERVAL_5MINUTE, "150 minute ago UTC")
                if len(Candles) == 30:
                    Data.append([Cur, Candles])
        if (TimeStamp == "15m"):
            for Cur in Test:
                Candles = client.get_historical_klines(Cur, Client.KLINE_INTERVAL_15MINUTE, "450 minute ago UTC")
                if len(Candles) == 30:
                    Data.append([Cur, Candles])
        if (TimeStamp == "30m"):
            for Cur in Test:
                Candles = client.get_historical_klines(Cur, Client.KLINE_INTERVAL_30MINUTE, "15 hour ago UTC")
                if len(Candles) == 30:
                    Data.append([Cur, Candles])
        if (TimeStamp == "1H"):
            for Cur in Test:
                Candles = client.get_historical_klines(Cur, Client.KLINE_INTERVAL_1HOUR, "30 hour ago UTC")
                if len(Candles) == 30:
                    Data.append([Cur, Candles])
        if (TimeStamp == "2H"):
            for Cur in Test:
                Candles = client.get_historical_klines(Cur, Client.KLINE_INTERVAL_2HOUR, "60 hour ago UTC")
                if len(Candles) == 30:
                    Data.append([Cur, Candles])
        if (TimeStamp == "4H"):
            for Cur in Test:
                Candles = client.get_historical_klines(Cur, Client.KLINE_INTERVAL_4HOUR, "5 day ago UTC")
                if len(Candles) == 30:
                    Data.append([Cur, Candles])
        if (TimeStamp == "6H"):
            for Cur in Test:
                Candles = client.get_historical_klines(Cur, Client.KLINE_INTERVAL_6HOUR, "180 hour ago UTC")
                if len(Candles) == 30:
                    Data.append([Cur, Candles])
        if (TimeStamp == "12H"):
            for Cur in Test:
                Candles = client.get_historical_klines(Cur, Client.KLINE_INTERVAL_12HOUR, "15 day ago UTC")
                if len(Candles) == 30:
                    Data.append([Cur, Candles])
        if (TimeStamp == "1D"):
            for Cur in Test:
                Candles = client.get_historical_klines(Cur, Client.KLINE_INTERVAL_1DAY, "30 day ago UTC")
                if len(Candles) == 30:
                    Data.append([Cur, Candles])
        if (TimeStamp == "3D"):
            for Cur in Test:
                Candles = client.get_historical_klines(Cur, Client.KLINE_INTERVAL_3DAY, "90 day ago UTC")
                if len(Candles) == 30:
                    Data.append([Cur, Candles])
        if (TimeStamp == "1W"):
            for Cur in Test:
                Candles = client.get_historical_klines(Cur, Client.KLINE_INTERVAL_1WEEK, "210 day ago UTC")
                if len(Candles) == 30:
                    Data.append([Cur, Candles])
        if (TimeStamp == "1M"):
            for Cur in Test:
                Candles = client.get_historical_klines(Cur, Client.KLINE_INTERVAL_1MONTH, "30 month ago UTC")
                if len(Candles) == 30:
                    Data.append([Cur, Candles])
        for i in range(0, len(Data)):
            Data[i][0] = Data[i][0].replace('USDT', '')
        if len(Data) != 0:
            self.log_2.setText(slog1)
            slog1 = " Download complete"
            self.log_1.setText(slog1)
        else:
            self.log_2.setText(slog1)
            slog1 = " Download failed"
            self.log_1.setText(slog1)

    def Empty(self):
        global pos
        exec("self.head_label_%s.setText('')" % (pos))
        for i in range (1, 15):  
            exec("self.label_%s_%s.setText('')" % (pos, i))
            for k in range (1, 4):
                exec("self.label_%s_%s_%s.setText('')" % (pos, i, k))

    def Ichimoku(self):
        IchiOut = []
        global slog1, pos
        self.log_2.setText(slog1)
        slog1 = " Calculating Ichimoku cross..."
        self.log_1.setText(slog1)
        for Cur in Data:
            Temp = [Cur[0]]
            for i in range(0,3):
                RHH = float(Cur[1][23][2])
                RLL = float(Cur[1][23][3])
                BHH = float(Cur[1][23][2])
                BLL = float(Cur[1][23][3])
                for j in range(4, 29):
                    RHH = max(float(Cur[1][j - i][2]), RHH)
                    RLL = min(float(Cur[1][j - i][3]), RLL)
                    if(j >= 21):
                        BHH = max(float(Cur[1][j - i][2]), BHH)
                        BLL = min(float(Cur[1][j - i][3]), BLL)
                RedFH = max(float(Cur[1][29 - i][2]), RHH)
                RedFL = min(float(Cur[1][29 - i][3]), RLL)
                RedSH = max(float(Cur[1][3 - i][2]), RHH)
                RedSL = min(float(Cur[1][3 - i][3]), RLL)
                BlueFH = max(float(Cur[1][29 - i][2]), BHH)
                BlueFL = min(float(Cur[1][29 - i][3]), BLL)
                BlueSH = max(float(Cur[1][20 - i][2]), BHH)
                BlueSL = min(float(Cur[1][20 - i][3]), BLL)
                RedF = (RedFH + RedFL) / 2
                RedS = (RedSH + RedSL) / 2
                BlueF = (BlueFH + BlueFL) / 2
                BlueS = (BlueSH + BlueSL) / 2
                if (RedF > BlueF or BlueS > RedS or RedS > RedF):
                    Temp.append(-1)
                else:
                    Temp.append((RedF - RedS) / RedF)
            IchiOut.append(Temp)
        Merge_Sort(IchiOut)
        exec("self.head_label_%s.setText('Ichimoku')" % (pos))
        y = min (14, len(IchiOut))
        for i in range (1, y + 1):  
            exec("self.label_%s_%s.setText('%s')" % (pos, i, IchiOut[i - 1][0]))
            for k in range (1, 4):
                exec("self.label_%s_%s_%s.setText('%s')" % (pos, i, k, IchiOut[i - 1][k]))
        if y <= len(IchiOut):
            self.log_2.setText(slog1)
            slog1 = " Ichimoku complete"
            self.log_1.setText(slog1)
        else:
            self.log_2.setText(slog1)
            slog1 = " Ichimoku failed"
            self.log_1.setText(slog1)

    def Reverse_Ichimoku(self):
        IchiOut = []
        global slog1, pos
        self.log_2.setText(slog1)
        slog1 = " Calculating R Ichimoku cross..."
        self.log_1.setText(slog1)
        for Cur in Data:
            Temp = [Cur[0]]
            for i in range(0,3):
                RHH = float(Cur[1][23][2])
                RLL = float(Cur[1][23][3])
                BHH = float(Cur[1][23][2])
                BLL = float(Cur[1][23][3])
                for j in range(4, 29):
                    RHH = max(float(Cur[1][j - i][2]), RHH)
                    RLL = min(float(Cur[1][j - i][3]), RLL)
                    if(j >= 21):
                        BHH = max(float(Cur[1][j - i][2]), BHH)
                        BLL = min(float(Cur[1][j - i][3]), BLL)
                RedFH = max(float(Cur[1][29 - i][2]), RHH)
                RedFL = min(float(Cur[1][29 - i][3]), RLL)
                RedSH = max(float(Cur[1][3 - i][2]), RHH)
                RedSL = min(float(Cur[1][3 - i][3]), RLL)
                BlueFH = max(float(Cur[1][29 - i][2]), BHH)
                BlueFL = min(float(Cur[1][29 - i][3]), BLL)
                BlueSH = max(float(Cur[1][20 - i][2]), BHH)
                BlueSL = min(float(Cur[1][20 - i][3]), BLL)
                RedF = (RedFH + RedFL) / 2
                RedS = (RedSH + RedSL) / 2
                BlueF = (BlueFH + BlueFL) / 2
                BlueS = (BlueSH + BlueSL) / 2
                if (RedF < BlueF or BlueS < RedS or RedS < RedF):
                    Temp.append(-1)
                else:
                    Temp.append((RedF - RedS) / (-1) * RedF)
            IchiOut.append(Temp)
        Merge_Sort(IchiOut)
        exec("self.head_label_%s.setText('Reverse Ichimoku')" % (pos))
        y = min (14, len(IchiOut))
        for i in range (1, y + 1):  
            exec("self.label_%s_%s.setText('%s')" % (pos, i, IchiOut[i - 1][0]))
            for k in range (1, 4):
                exec("self.label_%s_%s_%s.setText('%s')" % (pos, i, k, IchiOut[i - 1][k]))
        if y <= len(IchiOut):
            self.log_2.setText(slog1)
            slog1 = " Reverse Ichimoku complete"
            self.log_1.setText(slog1)
        else:
            self.log_2.setText(slog1)
            slog1 = " Reverse Ichimoku failed"
            self.log_1.setText(slog1)

    def Parabolic_SAR(self):
        PSAR_O = []
        global slog1, pos
        self.log_2.setText(slog1)
        slog1 = " Calculating PSAR ..."
        self.log_1.setText(slog1)
        for Cur in Data:
            Temp = [Cur[0]]
            L_Bull = 0
            L_Bear = 0

            AF = 0.02
            Max_AF = 0.2
            AF_C = 0.02
            PSAR = float(Cur[1][0][2])
            EP = float(Cur[1][0][3])
            Calc = AF * (EP - PSAR)
            Trend = "Bear"
            print(Cur[0])

            for i in range(1,30):
                Flag = 0
                #PSAR calculation
                if Trend == "Bull":
                    if float(Cur[1][i][2]) <= EP:
                        In_PSAR = PSAR + Calc
                        if i > 1:
                            In_PSAR = min(In_PSAR, float(Cur[1][i - 1][3]), float(Cur[1][i - 2][3]))
                        else:
                            In_PSAR = min(In_PSAR, float(Cur[1][0][3]))
                        if float(Cur[1][i][3]) > In_PSAR:
                            PSAR = In_PSAR
                        else:
                            PSAR = EP
                    else:
                        In_PSAR = PSAR + Calc + (AF * (EP - PSAR))
                        if i > 1:
                            In_PSAR = min(In_PSAR, float(Cur[1][i - 1][3]), float(Cur[1][i - 2][3]))
                        else:
                            In_PSAR = min(In_PSAR, float(Cur[1][0][3]))
                        if float(Cur[1][i][3]) > In_PSAR:
                            PSAR = In_PSAR
                        else:
                            PSAR = EP
                elif Trend == "Bear" :
                    if float(Cur[1][i][3]) >= EP:
                        In_PSAR = PSAR + Calc
                        if i > 1:
                            In_PSAR = max(In_PSAR, float(Cur[1][i - 1][2]), float(Cur[1][i - 2][2]))
                        else:
                            In_PSAR = max(In_PSAR, float(Cur[1][0][2]))
                        if float(Cur[1][i][2]) < In_PSAR:
                            PSAR = In_PSAR
                        else:
                            PSAR = EP
                    else:
                        In_PSAR = PSAR + Calc + (AF * (EP - PSAR))
                        if i > 1:
                            In_PSAR = max(In_PSAR, float(Cur[1][i - 1][2]), float(Cur[1][i - 2][2]))
                        else:
                            In_PSAR = max(In_PSAR, float(Cur[1][0][2]))
                        if float(Cur[1][i][2]) < In_PSAR:
                            PSAR = In_PSAR
                        else:
                            PSAR = EP
                #Trend calculation
                if float(Cur[1][i][4]) >= PSAR:
                    if Trend == "Bull":
                        Flag = 1
                    else:
                        L_Bull = i
                    Trend = "Bull"
                else:
                    if Trend == "Bear":
                        Flag = 1
                    else:
                        L_Bear = i
                    Trend = "Bear"
                #EP calculation
                LEP = EP
                if Trend == "Bull":
                    EP = max(EP, float(Cur[1][i][2]))
                elif Trend == "Bear":
                    EP = min(EP, float(Cur[1][i][3]))
                #AF calculation
                if Flag != 1:
                    AF_C = AF
                elif LEP != EP:
                    AF_C += AF
                    AF_C = min(AF_C, Max_AF)
                #Calc Calc
                Calc = AF_C * (EP - PSAR)
            #Temp garbage
            Temp.append(max(L_Bear, L_Bull))
            Temp.append(L_Bull)
            Temp.append(L_Bear)
            PSAR_O.append(Temp)
        Merge_Sort(PSAR_O)
        exec("self.head_label_%s.setText('Parabolic SAR')" % (pos))
        y = min (14, len(PSAR_O))
        for i in range (1, y + 1):  
            exec("self.label_%s_%s.setText('%s')" % (pos, i, PSAR_O[i - 1][0]))
            for k in range (1, 4):
                exec("self.label_%s_%s_%s.setText('%s')" % (pos, i, k, 30 - int(PSAR_O[i - 1][k])))
        if y <= len(PSAR_O):
            self.log_2.setText(slog1)
            slog1 = " Parabolic SAR complete"
            self.log_1.setText(slog1)
        else:
            self.log_2.setText(slog1)
            slog1 = " Parabolic SAR failed"
            self.log_1.setText(slog1)

if __name__ == '__main__':
    app = QW.QApplication([])
    W = Window()
    W.show()
    app.exec_()