## 2º STEP:
<p align="justify"><b>Formatting the company's termination date in Query Editor</b></p>
<p align="justify">Data field before</p>
<img width="124" alt="dt_before" src="https://user-images.githubusercontent.com/45472681/94950754-81ea2a00-04b9-11eb-9057-900012610143.png">
<p align="justify">Tor all null data records, we will assume the current date</p>
<p align="justify">The <b>DateTime.LocalNow () as datetime</b> function will return the current date</p>

```Python

M language 
if [DT_RET] = null
then
DateTime.LocalNow() as datetime
else [DT_RET]
```
